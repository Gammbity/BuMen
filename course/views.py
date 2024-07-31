from django.shortcuts import render
from rest_framework import generics
from course import models
from course import serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

class CategoryView(generics.ListAPIView):
    queryset = models.CategoryModel.objects.all()
    serializer_class = serializers.CategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['name']


class UserLessonView(generics.ListAPIView):
    queryset = models.UserLessonModel.objects.all()
    serializer_class = serializers.UserLessonSerializer