

from rest_framework import  serializers
from apps.seller.models import Seller
class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'
    def create(self,validated_data):
        user = Seller(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
class SellerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
    def to_representation(self, instance):
            return {
            'id': instance['id'],
            'name': instance['name'],
            'username': instance['username'],
            'email': instance['email']
        }
class UpdateSellerSerializer(serializers.ModelSerializer):
    class Meta:
         model = Seller
         fields = ('username', 'email', 'name', 'last_name')