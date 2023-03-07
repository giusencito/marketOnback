from apps.base.api import GeneralListApiView
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser
from apps.base.utils import validate_files
from rest_framework.decorators import action

from apps.products.api.serializers.product_serializers import ProductSerializer
class ProductListApiView(GeneralListApiView):
    serializer_class = ProductSerializer
class ProductCreateApiView(generics.CreateAPIView):
     serializer_class = ProductSerializer
     
     def post(self,request):
         serializer = self.serializer_class(data = request.data)
        
         if serializer.is_valid():
             serializer.save()
             return Response({'message':'product created'},status =  status.HTTP_201_CREATED)
         return Response({'message':'product can not be created'},status =  status.HTTP_400_BAD_REQUEST)
class ProductRetrievApiView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)
class ProductDelete(generics.DestroyAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)
    def delete(self,request,pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message':'product deleted'},status =  status.HTTP_201_CREATED)
        return Response({'message':'product can not be deleted'},status =  status.HTTP_400_BAD_REQUEST)
class ProductUpdate (generics.UpdateAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)
    def patch(self, request,pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product_serializer=self.serializer_class(product)
            return Response(product_serializer.data,status.HTTP_200_OK)
        return Response({'error':'product can not be deleted'},status =  status.HTTP_400_BAD_REQUEST)
   
class ProductViewSet(viewsets.ModelViewSet):
     serializer_class = ProductSerializer
     parser_classes = (JSONParser, MultiPartParser, )
     def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()
     def list(self, request):
        product_serializer = self.get_serializer(self.get_queryset(), many=True)
        data = {
            "total": self.get_queryset().count(),
            "totalNotFiltered": self.get_queryset().count(),
            "rows": product_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK) 
     def create(self, request):
            
        data = validate_files(request.data,'image')
        serializer = self.serializer_class(data=data)     
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Producto creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message':'', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
     def update(self, request, pk=None):
         if self.get_queryset(pk):
             # send information to serializer referencing the instance
             data = validate_files(request.data, 'image', True)
             product_serializer = self.serializer_class(self.get_queryset(pk), data=data)            
             if product_serializer.is_valid():
                product_serializer.save()
                return Response({'message':'Producto actualizado correctamente!'}, status=status.HTTP_200_OK)
             return Response({'message':'', 'error':product_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
     def destroy(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first() # get instance        
        if product:
            product.state = False
            product.save()
            return Response({'message':'Producto eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe un Producto con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)
    
    
     @action(detail=True, methods=['get'])
     def getproductbyName(self,request,pk=None):
        self.queryset = self.serializer_class().Meta.model.objects.filter(state=True).filter(name=pk)
        assitans =  self.queryset
        assitans_serializer = self.serializer_class(assitans, many=True)
        data = {
            
            "total": self.get_queryset().count(),
            "rows": assitans_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
    