from rest_framework.routers import DefaultRouter
from apps.assistant.api.viewset import AssitantViewSet
router = DefaultRouter()
router.register(r'AssitantViewSet',AssitantViewSet,basename='AssitantView')
urlpatterns = router.urls