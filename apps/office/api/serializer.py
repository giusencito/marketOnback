from rest_framework import serializers
from apps.office.models import Office
class OfficeSerializer(serializers.ModelSerializer):
    def to_representation(self,instance):
            return {
                'id': instance.id,
                'name': instance.name, 
                'office_boss': f'Boss {instance.boss.name} {instance.boss.last_name}'
            }
    def validate_boss(self, value):
        if value == '' or value == None:
                raise serializers.ValidationError("Debe ingresar una jefe.")
        return value
    def validate(self, data):
        if 'boss' not in data.keys():
            raise serializers.ValidationError({
                "Boss": "Debe ingresar un jefe"
            })
        return data
             
    class Meta:
        model = Office
        exclude = ('state','created_date','modified_date','deleted_date')
