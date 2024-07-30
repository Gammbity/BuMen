from django.urls import path
from course import views

urlpatterns = [
    path('user/lessons/', views.UserLessonView.as_view())
]
