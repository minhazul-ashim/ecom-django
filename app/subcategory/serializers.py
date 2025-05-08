from rest_framework import serializers
from subcategory.models import Subcategory
from category.serializers import SimpleCategorySerializer
    
class SimpleSubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'thumb']

class SubcategorySerializer(serializers.ModelSerializer):
    category_detail = SimpleCategorySerializer(source='category', read_only=True)
    class Meta:
        model = Subcategory
        fields = '__all__'

    def create(self, validated_data):
        return Subcategory.objects.create(**validated_data)