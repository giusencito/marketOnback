from rest_framework.routers import DefaultRouter
from apps.report.api.viewsets import ReportViewSet
router = DefaultRouter()
router.register(r'ReportViewSet',ReportViewSet,basename='ReportView')
urlpatterns = router.urls