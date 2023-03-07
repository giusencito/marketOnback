from rest_framework import serializers
from apps.movement.models import Movement

class MovementSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return {
             'id': instance.id,
             'quantity': instance.quantity,
             'new_left': instance.new_left,
             'date': instance.date,
             'product': instance.product.name,
             'inventory': instance.inventory.id,
             'assistant': f'{instance.assistant.name} {instance.assistant.last_name}',
             'seller': f'{instance.seller.name} {instance.seller.last_name}',
        }
    def validate_product(self, value):
       if value == '' or value == None:
                raise serializers.ValidationError("Debe ingresar un producto.")
       return value
    def validate_inventory(self, value):
      if value == '' or value == None:
                raise serializers.ValidationError("Debe ingresar un inventario.")
      return value
    def validate_assitant(self, value):
      if value == '' or value == None:
                raise serializers.ValidationError("Debe ingresar un assistant.")
      return value
    def validate_seller(self, value):
      if value == '' or value == None:
                raise serializers.ValidationError("Debe ingresar un seller.")
      return value
    class Meta:
        model = Movement
        exclude = ('state','created_date','modified_date','deleted_date')