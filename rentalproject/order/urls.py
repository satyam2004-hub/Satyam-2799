from django.urls import path
from .import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    
]
router=DefaultRouter()
router.register("order",views.OrderViewSet)
urlpatterns += router.urls
