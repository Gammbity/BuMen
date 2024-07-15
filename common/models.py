from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor_uploader.fields import RichTextUploadingField


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True

class SettingsModel(BaseModel):
    objects = models.Manager()
    email = models.EmailField()
    links = models.URLField()   
    appstore_link = models.URLField(null=True, blank=True)
    playmarket_link = models.URLField(null=True, blank=True)
    contact_phone = models.CharField(max_length=13)
    longitude = models.FloatField()
    latitude = models.FloatField()
    location_text = models.TextField()
    telegram = models.CharField(max_length=66, null=True, blank=True)
    instagram = models.CharField(max_length=66, null=True, blank=True)
    linkedin = models.CharField(max_length=66, null=True, blank=True)
    facebook = models.CharField(max_length=66, null=True, blank=True)

class UserContactAppModel(BaseModel):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    message = models.TextField(max_length=500)
    is_contacted = models.BooleanField(default=False)

    class Meta:
        ordering = ['is_contacted', 'created_at']
        verbose_name = _('User Contact Application') 
        verbose_name_plural = _('User Contact Applications') 

class PartnerModel(BaseModel):
    image = models.ImageField(upload_to='common/partner/%Y/$m/')
    link = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = _('partner')
        verbose_name_plural = _('partners')

class NewModel(BaseModel):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()
    banner = models.ImageField(upload_to='common/news/%Y/%m/')
    top = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('new')
        verbose_name_plural = _('news')

class PageModel(BaseModel):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()

class QuoteModel(BaseModel):
    author = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        verbose_name = _('quote')
        verbose_name_plural = _('quotes')

class AdvertisingModel(BaseModel):
    image = models.ImageField(upload_to='advertising/%Y/%m/')
    link = models.URLField()
    
    class Meta:
        verbose_name = _('advertising')
        verbose_name_plural = _('advertisements')


class FAQModel(BaseModel):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    order = models.PositiveIntegerField(blank=True)

    class Meta:
        verbose_name = _('FAQ')
        verbose_name_plural = _('FAQs')

    def save(self, *args, **kwargs):
        if self.order is None:
            order = 1
            last_faq = FAQModel.objects.order_by('order').last()
            if last_faq:
                order = last_faq.order + 1  
            self.order = order

        super().save(*args, **kwargs)

class AboutAppModel(BaseModel):
    caption = models.CharField(max_length=255)
    text = models.TextField()
    order = models.PositiveIntegerField(blank=True)

    class Meta:
        verbose_name = _('about app')
        verbose_name_plural = _('advertisements')
     
    def save(self, *args, **kwargs):
        if self.order is None:
            order = 1
            last_about_app = AboutAppModel.objects.order_by('order').last()
            if last_about_app:
                order = last_about_app.order + 1  
            self.order = order

        super().save(*args, **kwargs)