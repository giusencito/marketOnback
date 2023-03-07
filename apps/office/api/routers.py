from rest_framework.routers import DefaultRouter
from apps.office.api.viewset import OfficeViewSet
router = DefaultRouter()
router.register(r'OfficeViewSet',OfficeViewSet,basename='OfficeView')
urlpatterns = router.urls