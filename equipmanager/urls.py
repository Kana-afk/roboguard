from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EquipmentViewSet, DataViewSet, AlertViewSet

router = DefaultRouter()
router.register(r'equipment', EquipmentViewSet)
router.register(r'data', DataViewSet)
router.register(r'alerts', AlertViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
