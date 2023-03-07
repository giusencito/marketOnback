from rest_framework.routers import DefaultRouter
from apps.products.api.viewsets.product_view import ProductViewSet
from apps.products.api.viewsets.general_views import CategoryViewSet

router = DefaultRouter()

router.register(r'productsSet',ProductViewSet,basename='productView')
router.register(r'categorySet',CategoryViewSet,basename='categoryView')

urlpatterns = router.urls