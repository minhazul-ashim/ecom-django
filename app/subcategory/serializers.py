from rest_framework.serializers import ModelSerializer
from subcategory.models import Subcategory
from category.serializers import CategorySerializer

class SubcategorySerializer(ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Subcategory
        fields = '__all__'

    def create(self, validated_data):
        return Subcategory.objects.create(**validated_data)