from rest_framework.routers import DefaultRouter
from apps.seller.api.viewsets import SellerViewSet
router = DefaultRouter()
router.register(r'SellerViewSet',SellerViewSet,basename='SellerView')
urlpatterns = router.urls