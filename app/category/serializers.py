from rest_framework import serializers
from category.models import Category

class SimpleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'thumb']

class CategorySerializer(serializers.ModelSerializer):
    from subcategory.serializers import SimpleSubcategorySerializer #Iimporting here to avoid circular import issues;
    subcategories = SimpleSubcategorySerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = '__all__'

    def create(self, validated_data):
        return Category.objects.create(**validated_data)