from rest_framework import serializers
from apps.stock.models import Stock

class StockSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return {
            
             'id': instance.id,
             'stock': instance.stock,
             'product': instance.product.name,
             'inventory': instance.inventory.id,     
        }
    def validate_product(self, value):
           if value == '' or value == None:
                raise serializers.ValidationError("Debe ingresar un producto.")
           return value
    def validate_inventory(self, value):
      if value == '' or value == None:
                raise serializers.ValidationError("Debe ingresar un inventario.")
      return value
    class Meta:
        model = Stock
        exclude = ('state','created_date','modified_date','deleted_date')