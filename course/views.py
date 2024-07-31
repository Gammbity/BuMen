from rest_framework import generics
from course import models
from course import serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import status

class LessonView(generics.ListAPIView):
    serializer_class = serializers.LessonSerializer

    def get_queryset(self):
        theme_id = self.kwargs['theme_id']
        lesson_type = self.kwargs['lesson_type']
        queryset = models.LessonModel.objects.filter(theme=theme_id, type=lesson_type)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset:
            theme, type = str(queryset[0]).split("|")
            return Response({
                'theme': theme,
                'type': type
            }, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

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