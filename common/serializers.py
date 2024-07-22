from rest_framework import serializers
from common import models

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SettingsModel
        fields = [
            'objects',
            'email',
            'links',
            'appstore_link',
            'playmarket_link',
            'contact_phone',
            'longitude',
            'latitude',
            'location_text',
            'telegram',
            'instagram',
            'linkedin',
            'facebook'
        ]

class UserConCreateSerializer(serializers.ModelSerializer): 
    class Meta:
        model = models.UserContactAppModel
        fields = [
            'full_name',
            'phone',
            'message'
        ]

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PartnerModel
        fields = ['image', 'link']

class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NewModel
        fields = ['slug', 'title', 'content', 'banner', 'hit_count', 'top']

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PageModel
        fields = ['slug', 'title', 'content']

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.QuoteModel
        fields = ['author', 'content']

class AdvertisingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AdvertisingModel
        fields = ['image', 'link']

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FAQModel
        fields = ['question', 'answer']

class AboutAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AboutAppModel
        fields = ['caption', 'text']