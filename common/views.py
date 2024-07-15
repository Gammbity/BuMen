from common import serializers
from common import models
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

class SettingsView(generics.GenericAPIView):
    queryset = models.SettingsModel.objects.all()
    serializer_class = serializers.SettingsSerializer

    def get(self, request, *args, **kwargs):
        setting = self.get_queryset().first()
        serializer = self.get_serializer(setting)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserContactView(generics.CreateAPIView):
    queryset = models.UserContactAppModel.objects.all()
    serializer_class = serializers.UserConSerializer

class PartnerView(generics.ListAPIView):
    queryset = models.PartnerModel.objects.all()
    serializer_class = serializers.PartnerSerializer

class NewView(generics.ListAPIView):
    queryset = models.NewModel.objects.all()
    serializer_class = serializers.NewSerializer

class PageView(generics.RetrieveAPIView):
    queryset = models.PageModel.objects.all()
    serializer_class = serializers.PageSerializer

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