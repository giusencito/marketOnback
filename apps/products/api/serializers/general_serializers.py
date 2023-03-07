from apps.products.models import Category,Product

from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        exclude = ('state','created_date','modified_date','deleted_date')