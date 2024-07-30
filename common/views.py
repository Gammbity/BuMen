from common import serializers
from common import models
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.rest_framework.backends import DjangoFilterBackend
from common import filters
from common import throttling
from common.tasks import add_news_view
from common.utility import get_ip


class ContactCategoryView(generics.ListAPIView):
    queryset = models.ContactCategoryModel.objects.all()
    serializer_class = serializers.ContactCategorySerializer

class SettingsView(generics.GenericAPIView):
    queryset = models.SettingsModel.objects.all()
    serializer_class = serializers.SettingsSerializer

    @method_decorator(cache_page(5*60))
    def get(self, request, *args, **kwargs):
        setting = self.get_queryset().first()
        serializer = self.get_serializer(setting)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserContactView(generics.CreateAPIView):
    queryset = models.UserContactAppModel.objects.all()
    serializer_class = serializers.UserConCreateSerializer
    throttle_classes = [throttling.CreateContactAppIPThrottle,
                        throttling.CreateContactAppNumThrottle]

class PartnerView(generics.ListAPIView):
    queryset = models.PartnerModel.objects.all()
    serializer_class = serializers.PartnerSerializer

class NewView(generics.ListAPIView):
    queryset = models.NewModel.objects.order_by('-created_at')
    serializer_class = serializers.NewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.NewsFilter

class NewDetailView(generics.RetrieveAPIView):
    queryset = models.NewModel.objects.all()
    serializer_class = serializers.NewSerializer
    lookup_field = 'slug'

    def get_object(self):
        news = super().get_object()
        news_id = news.id
        visitor_id = self.request.META.get('HTTP_X_VISITOR_ID')
        ip = get_ip(self.request)

        if visitor_id:
            add_news_view.delay(news_id, visitor_id, ip)

        return news

class PageView(generics.RetrieveAPIView):
    queryset = models.PageModel.objects.all()
    serializer_class = serializers.PageSerializer
    lookup_field = 'slug'

class QuoteView(generics.ListAPIView):
    queryset = models.QuoteModel.objects.all()
    serializer_class = serializers.QuoteSerializer

class AdvertisingView(generics.ListAPIView):
    queryset = models.AdvertisingModel.objects.all()
    serializer_class = serializers.AdvertisingSerializer

class FAQView(generics.ListAPIView):
    queryset = models.FAQModel.objects.all()
    serializer_class = serializers.FAQSerializer

class AboutAppView(generics.ListAPIView):
    queryset = models.AboutAppModel.objects.all()
    serializer_class = serializers.AboutAppSerializer