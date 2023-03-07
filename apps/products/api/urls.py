
from django.urls import path
from apps.products.api.viewsets.general_views import CategoryListApiView
from apps.products.api.viewsets.product_view import ProductListApiView,ProductCreateApiView,ProductRetrievApiView,ProductDelete
urlpatterns = [
    path('categories/', CategoryListApiView.as_view(), name = 'category'),
    path('products/list', ProductListApiView.as_view(), name = 'product'),
    path('products/create', ProductCreateApiView.as_view(), name = 'productcreate'),
     path('products/retrieve/<int:pk>', ProductRetrievApiView.as_view(), name = 'productretrieve'),
      path('products/destroy/<int:pk>', ProductDelete.as_view(), name = 'productdestroy'),
     
]