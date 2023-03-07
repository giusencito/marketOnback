
from rest_framework import  serializers
from apps.boss.models import Boss
class BossSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boss
        fields = '__all__'
    def create(self,validated_data):
        user = Boss(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
class BossListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boss
    def to_representation(self, instance):
            return {
            'id': instance['id'],
            'name': instance['name'],
            'username': instance['username'],
            'email': instance['email']
        }
class UpdateBossSerializer(serializers.ModelSerializer):
    class Meta:
         model = Boss
         fields = ('username', 'email', 'name', 'last_name')