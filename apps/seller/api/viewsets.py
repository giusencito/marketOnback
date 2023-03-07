from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from  apps.seller.models import Seller
from apps.seller.api.serializer import (SellerSerializer,SellerListSerializer,UpdateSellerSerializer)
class SellerViewSet(viewsets.GenericViewSet):
  
    serializer_class = SellerSerializer
    list_serializer_class = SellerListSerializer
    queryset = None
    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)
    def get_queryset(self):
           if self.queryset is None:
               self.queryset = self.serializer_class().Meta.model.objects.filter(is_active=True).values('id', 'username', 'email', 'name')
           return self.queryset
    def list(self, request):
         users = self.get_queryset()
         users_serializer = self.list_serializer_class(users, many=True)
         return Response(users_serializer.data, status=status.HTTP_200_OK)
     
    

    def create(self, request):
         user_serializer = self.serializer_class(data=request.data)
         if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'message': 'Usuario registrado correctamente.'
            }, status=status.HTTP_201_CREATED)
         return Response({
            'message': 'Hay errores en el registro',
            'errors': user_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self, request,pk=None):
        user = self.get_object(pk)
        user_serializer = self.serializer_class(user)
        return Response(user_serializer.data)
    def update(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = UpdateSellerSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'message': 'Usuario actualizado correctamente'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'Hay errores en la actualización',
            'errors': user_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
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
    def findbyusername(self, request,pk=None):
        self.queryset = self.serializer_class().Meta.model.objects.filter(is_active=True).filter(username=pk)
        boss = self.get_queryset()
        assitans_serializer = self.serializer_class(boss, many=True)
        return Response(assitans_serializer.data, status=status.HTTP_200_OK)