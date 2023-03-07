
from rest_framework import  serializers
from apps.assistant.models import Assistant
class AssitantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistant
        fields = '__all__'
    def create(self,validated_data):
        user = Assistant(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
class AssitantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistant
    def to_representation(self, instance):
            #bossassname = instance['bossassit']['name']
            #bossasslastname= instance['bossassit']['last_name']
            print(instance['bossassit'])
            print('uuee')
            return {
            'id': instance['id'],
            'name': instance['name'],
            'username': instance['username'],
            'email': instance['email'],
            'bossassit': instance['bossassit']
            
        }
class UpdateAssitantSerializer(serializers.ModelSerializer):
    class Meta:
         model = Assistant
         fields = ('username', 'email', 'name', 'last_name')