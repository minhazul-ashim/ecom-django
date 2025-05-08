from dataclasses import fields
from rest_framework import serializers
from product.models import Product, ProductVariant, PriceVariant
from category.serializers import SimpleCategorySerializer
from subcategory.serializers import SimpleSubcategorySerializer

# ------------------------Product Serializers-------------------------------
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

# ------------------------Product Variant Serializers-------------------------------
class SimpleProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ['id', 'name', 'description', 'price', 'stock', 'image']

class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = '__all__'

    def create(self, validated_data):
        return ProductVariant.objects.create(**validated_data)

# ------------------------Price Varaint Serializers-------------------------------
class SimplePriceVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceVariant
        fields = ['id', 'description', 'min_qty', 'max_qty', 'price']

class PriceVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceVariant
        fields = '__all__'

    def create(self, validated_data):
        return PriceVariant.objects.create(**validated_data)