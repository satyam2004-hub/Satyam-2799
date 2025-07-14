from django.contrib import admin
from django.urls import path, include

from djangodaytwo import views

urlpatterns = [
    path('home/', views.home),
    path('contact/', views.contact),
    path('about/', views.about),
]
