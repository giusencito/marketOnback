

from rest_framework import serializers
from apps.report.models import Report
class ReportSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'description': instance.description, 
            'start': instance.start, 
            'finish': instance.finish, 
            'assistant': f' Assistant {instance.assistant.name} {instance.assistant.last_name}',
            'inventory': f' Inventory with {instance.inventory.quantity}',
        }
    def validate_assistant(self, value):
        if value == '' or value == None:
                raise serializers.ValidationError("Debe ingresar un assistant.")
        return value
    def validate_inventory(self, value):
        if value == '' or value == None:
                raise serializers.ValidationError("Debe ingresar un inventario.")
        return value
    def validate(self, data):
        if 'assistant' not in data.keys():
            raise serializers.ValidationError({
                "Inventory": "Debe ingresar un assistant"
            })
        if 'inventory' not in data.keys():
                raise serializers.ValidationError({
                "Inventory": "Debe ingresar un inventario"
            })
        return data
    class Meta:
        model = Report
        exclude = ('state','created_date','modified_date','deleted_date')