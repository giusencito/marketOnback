from rest_framework.routers import DefaultRouter
from apps.inventory.api.viewsets import InventoryViewSet
router = DefaultRouter()
router.register(r'InventoryViewSet',InventoryViewSet,basename='InventoryView')
urlpatterns = router.urls