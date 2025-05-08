from rest_framework import serializers
from product.models import Product
from category.serializers import SimpleCategorySerializer
from subcategory.serializers import SimpleSubcategorySerializer

class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'image', 'description']

class ProductSerializer(serializers.ModelSerializer):
    category = SimpleCategorySerializer(source='category_id', read_only=True)
    subcategory = SimpleSubcategorySerializer(source='subcategory_id', read_only=True)
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        return Product.objects.create(**validated_data)