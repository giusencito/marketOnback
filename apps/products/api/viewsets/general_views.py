from apps.products.models import Category
from apps.base.api import GeneralListApiView
from apps.products.api.serializers.general_serializers import CategorySerializer
from rest_framework import viewsets
class CategoryListApiView(GeneralListApiView):
    serializer_class = CategorySerializer
    
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    
    
    
    