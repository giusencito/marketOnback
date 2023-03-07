
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from apps.office.api.serializer import OfficeSerializer
from rest_framework.decorators import action
class OfficeViewSet(viewsets.ModelViewSet):
    serializer_class = OfficeSerializer
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()
    def list(self, request):
        boss_serializer = self.get_serializer(self.get_queryset(), many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": boss_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Producto creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self, request, pk=None):
        product = self.get_queryset(pk)
        if product:
            product_serializer = OfficeSerializer(product)
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        return Response({'error':'No existe un Producto con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message':'Producto eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe un Producto con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)
    @action(detail=True, methods=['get'])
    def getofficebyboss(self,request,pk=None):
        boss_serializer = self.get_serializer(self.get_queryset().filter(boss_id = pk), many=True)
        data = {
            "total": self.get_queryset().filter(boss_id = pk).count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": boss_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)