from rest_framework.routers import DefaultRouter
from apps.stock.api.viewsets import StockViewSet
router = DefaultRouter()
router.register(r'StockViewSet',StockViewSet,basename='StockView')
urlpatterns = router.urls