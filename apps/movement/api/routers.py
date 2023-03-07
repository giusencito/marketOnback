from rest_framework.routers import DefaultRouter
from apps.movement.api.viewsets import MovementViewSet
router = DefaultRouter()
router.register(r'MovementViewSet',MovementViewSet,basename='MovementView')
urlpatterns = router.urls