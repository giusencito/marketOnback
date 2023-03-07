from rest_framework import serializers
from apps.products.models import Product
from apps.products.api.serializers.general_serializers import CategorySerializer
class ProductSerializer(serializers.ModelSerializer):
    def to_representation(self,instance):
            return {
                'id': instance.id,
                'name': instance.name,            
                'description': instance.description,
                'image': instance.image.url if instance.image != '' else '',
                'category_product': instance.category.description if instance.category is not None else ''
            }
    class Meta:
        model = Product
        exclude = ('state','created_date','modified_date','deleted_date')


