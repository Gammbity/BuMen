from django.shortcuts import render
from rest_framework import generics
from course import models
from course import serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class LessonThemesView(generics.ListAPIView):
    queryset = models.LessonThemeModel.objects.all()
    serializer_class = serializers.LessonThemeSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category']

class CategoryView(generics.ListAPIView):
    queryset = models.CategoryModel.objects.all()
    serializer_class = serializers.CategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name']


class UserLessonView(generics.ListAPIView):
    queryset = models.UserLessonModel.objects.all()
    serializer_class = serializers.UserLessonSerializer