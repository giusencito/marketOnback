from apps.stock.api.serializer import StockSerializer
from rest_framework.decorators import action
from apps.stock.models import Stock 
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
class StockViewSet(viewsets.ModelViewSet):
    model = Stock
    serializer_class = StockSerializer
    queryset = None
    def get_object(self, pk):
            return get_object_or_404(self.model, pk=pk)
    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.get_serializer().Meta.model.objects.filter(state=True)
        return self.queryset
    def list(self, request):
        inventory_serializer = self.get_serializer(self.get_queryset(), many=True)
        data = {
            "total": self.get_queryset().count(),
            "rows": inventory_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Stock creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk=None):
        user_destroy = self.model.objects.filter(id=pk).update(is_active=False)
        if user_destroy == 1:
            return Response({
                'message': 'Usuario eliminado correctamente'
            })
        return Response({
            'message': 'No existe el usuario que desea eliminar'
        }, status=status.HTTP_404_NOT_FOUND)
    @action(detail=True, methods=['get'])
    def getstockbyproduct(self,request,pk=None):
        self.queryset = self.serializer_class().Meta.model.objects.filter(state=True).filter(product_id=pk)
        assitans = self.get_queryset()
        assitans_serializer = self.serializer_class(assitans, many=True)
        data = {
            
            "total": self.get_queryset().count(),
            "rows": assitans_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
    @action(detail=True, methods=['get'])
    def getstockbyinventory(self,request,pk=None):
        self.queryset = self.serializer_class().Meta.model.objects.filter(state=True).filter(inventory_id=pk)
        assitans = self.get_queryset()
        assitans_serializer = self.serializer_class(assitans, many=True)
        data = {
            
            "total": self.get_queryset().count(),
            "rows": assitans_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
    def update(self, request, pk=None):
      
           
             data = request.data
             product_serializer = self.serializer_class(self.get_object(pk), data=data)            
             if product_serializer.is_valid():
                product_serializer.save()
                return Response({'message':'Producto actualizado correctamente!'}, status=status.HTTP_200_OK)
             return Response({'message':'', 'error':product_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)