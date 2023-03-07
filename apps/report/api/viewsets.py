from apps.report.api.serializer import ReportSerializer
from rest_framework.decorators import action
from apps.report.models import Report
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
class ReportViewSet(viewsets.ModelViewSet):
    model = Report
    serializer_class = ReportSerializer
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
            return Response({'message': 'Producto creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self, request, pk=None):
        inventtory = self.get_object(pk)
        inventtory_serializer = self.serializer_class(inventtory)
        return Response(inventtory_serializer.data)

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
    def getreportbyinventory(self,request,pk=None):
        self.queryset = self.serializer_class().Meta.model.objects.filter(state=True).filter(inventory_id=pk)
        assitans = self.get_queryset()
        assitans_serializer = self.serializer_class(assitans, many=True)
        data = {
            
            "total": self.get_queryset().count(),
            "rows": assitans_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
    @action(detail=True, methods=['get'])
    def getassitantbyinventory(self,request,pk=None):
        self.queryset = self.serializer_class().Meta.model.objects.filter(state=True).filter(assistant_id=pk)
        assitans = self.get_queryset()
        assitans_serializer = self.serializer_class(assitans, many=True)
        data = {
            
            "total": self.get_queryset().count(),
            "rows": assitans_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)


