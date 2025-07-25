from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet

router = DefaultRouter()
router.register(r'payment', PaymentViewSet)

urlpatterns = router.urls
