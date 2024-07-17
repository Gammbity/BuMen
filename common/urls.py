from django.urls import path
from common import views

urlpatterns = [
    path('setting/', views.SettingsView.as_view()),
    path('user-contact-application/create/', views.UserContactView.as_view()),
    path('partners/', views.PartnerView.as_view()),
    path('news/', views.NewView.as_view()),
    path('new/<str:slug>/', views.NewGetView.as_view()),
    path('page/<str:slug>/', views.PageView.as_view()),
    path('quote/', views.QuoteView.as_view()),
    path('advertising/', views.AdvertisingView.as_view()),
    path('FAQ/', views.FAQView.as_view()),
    path('about-app/', views.AboutAppView.as_view()),
]
