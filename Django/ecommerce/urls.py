from django.urls import path
from ecommerce import views

urlpatterns = [
    path('Home/', views.home),
]

