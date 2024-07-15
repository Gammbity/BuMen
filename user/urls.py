from django.urls import path
from user import views

urlpatterns = [
    path('user-create/', views.UserCreateView.as_view()),    
]
