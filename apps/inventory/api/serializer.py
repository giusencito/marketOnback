from rest_framework import serializers
from apps.inventory.models import Inventory

class InventorySerializer(serializers.ModelSerializer):
    def to_representation(self,instance):
            return {
                'id': instance.id,
                'quantity': instance.quantity, 
                'inventory_office': f'{instance.office.name} Office'
            }
    def validate_inventory(self, value):
        if value == '' or value == None:
                raise serializers.ValidationError("Debe ingresar un Inventory.")
        return value
    def validate(self, data):
        if 'office' not in data.keys():
            raise serializers.ValidationError({
                "Inventory": "Debe ingresar un Inventory"
            })
        return data
    class Meta:
        model = Inventory
        exclude = ('state','created_date','modified_date','deleted_date')