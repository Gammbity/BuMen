from celery import shared_task
from common import models
from django.utils import timezone
from datetime import timedelta
from django.utils.translation import gettext_lazy as _
from django.db.models import F


@shared_task
def add_news_view(news_id, visitor_id, ip):
    count = models.NewsViewModel.objects.filter(ip=ip, created_at__gt=timezone.now() - timedelta(hours=1)).count()
    if count >= 1000:
        return _(f"{news_id}: {ip} oxirgi soat ichida 1000 ta ko'rish yaratgan.")
    if models.NewsViewModel.objects.filter(visitor_id=visitor_id, news_id=news_id).exists():
        return _(f"{news_id}: {visitor_id} bu yangilikni avval ko'rgan.")
    
    models.NewsViewModel.objects.create(
        news_id=news_id,
        visitor_id=visitor_id,
        ip=ip
    )

    models.NewModel.objects.filter(id=news_id).update(
        hit_count = F('hit_count') + 1
    )

@shared_task
def news_views_cleaner():
    count, _= models.NewsViewModel.objects.filter(
        created_at__lt=timezone.now() - timedelta(days=14)
    ).delete()
        
    return f"{count} NewsViewModels deleted!"