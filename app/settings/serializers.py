from rest_framework import serializers
from settings.models import *

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = '__all__'

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)

class AttributeItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttributeItem
        fields = '__all__'

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)
    
class UnitTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = UnitType
        fields = '__all__'

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)
    
class StoreInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreInfo
        fields = '__all__'

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)
    
class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)
    
class ExtraPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraPage
        fields = '__all__'

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)
    
class StoreGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreGallery
        fields = '__all__'

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)
    
class StoreUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreUpload
        fields = '__all__'

    def create(self, validated_data):
        return self.Meta.model.objects.create(**validated_data)