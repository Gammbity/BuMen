from django.contrib import admin
from django.http import HttpRequest
from common import models

@admin.register(models.SettingsModel)
class SettingsAdmin(admin.ModelAdmin):

    def has_add_permission(self, request: HttpRequest) -> bool: 
        if models.SettingsModel.objects.exists():
            return False
        return True
    
    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return False

@admin.register(models.UserContactAppModel)
class UserContactAppAdmin(admin.ModelAdmin):
    list_display = ['full_name']
    list_display_links = ['full_name']

@admin.register(models.PartnerModel)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['id', 'link']
    list_display_links = ['id', 'link']

@admin.register(models.NewModel)
class NewAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']

@admin.register(models.PageModel)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']

@admin.register(models.QuoteModel)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['author']
    list_display_links = ['author']

@admin.register(models.AdvertisingModel)
class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ['id', 'link']
    list_display_links = ['id', 'link']

@admin.register(models.FAQModel)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'answer']
    list_display_links = ['id', 'question', 'answer']

@admin.register(models.AboutAppModel)
class AboutAppAdmin(admin.ModelAdmin):
    list_display = ['caption', 'text']
    list_display_links = ['caption', 'text']