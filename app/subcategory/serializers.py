from rest_framework import serializers
from subcategory.models import Subcategory

class SimpleSubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'thumb']

class SubcategorySerializer(serializers.ModelSerializer):
    from category.serializers import SimpleCategorySerializer #Importing here to avoid circular import issues;
    category = SimpleCategorySerializer()
    class Meta:
        model = Subcategory
        fields = '__all__'

    def create(self, validated_data):
        return Subcategory.objects.create(**validated_data)