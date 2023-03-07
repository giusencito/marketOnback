from rest_framework.routers import DefaultRouter
from apps.boss.api.viewsets import BosssViewSet
router = DefaultRouter()
router.register(r'BosssViewSet',BosssViewSet,basename='BossView')
urlpatterns = router.urls