from django.shortcuts import render
from rest_framework import viewsets
from app.permissions import IsAdminForUnsafeMethods
from settings.serializers import *
from settings.models import *
from app.utils import format_exception

# Create your views here.
class AttributeViewset(viewsets.ModelViewSet):
    permission_classes = [IsAdminForUnsafeMethods]
    serializer_class = AttributeSerializer
    queryset = Attribute.objects.all()

    def handle_exception(self, exc):
        return format_exception(exc, self.request)
    
class AttributeItemViewset(viewsets.ModelViewSet):
    permission_classes = [IsAdminForUnsafeMethods]
    serializer_class = AttributeItemSerializer
    queryset = AttributeItem.objects.all()

    def handle_exception(self, exc):
        return format_exception(exc, self.request)

class UnitTypeViewset(viewsets.ModelViewSet):
    permission_classes = [IsAdminForUnsafeMethods]
    serializer_class = UnitTypeSerializer
    queryset = UnitType.objects.all()

    def handle_exception(self, exc):
        return format_exception(exc, self.request)
    
class StoreInfoViewset(viewsets.ModelViewSet):
    permission_classes = [IsAdminForUnsafeMethods]
    serializer_class = StoreInfoSerializer
    queryset = StoreInfo.objects.all()

    def handle_exception(self, exc):
        return format_exception(exc, self.request)
    
class SocialMediaViewset(viewsets.ModelViewSet):
    permission_classes = [IsAdminForUnsafeMethods]
    serializer_class = SocialMediaSerializer
    queryset = SocialMedia.objects.all()

    def handle_exception(self, exc):
        return format_exception(exc, self.request)
    
class ExtraPageViewset(viewsets.ModelViewSet):
    permission_classes = [IsAdminForUnsafeMethods]
    serializer_class = ExtraPageSerializer
    queryset = ExtraPage.objects.all()

    def handle_exception(self, exc):
        return format_exception(exc, self.request)
    
class StoreGalleryViewset(viewsets.ModelViewSet):
    permission_classes = [IsAdminForUnsafeMethods]
    serializer_class = StoreGallerySerializer
    queryset = StoreGallery.objects.all()

    def handle_exception(self, exc):
        return format_exception(exc, self.request)
    
class StoreUploadViewset(viewsets.ModelViewSet):
    permission_classes = [IsAdminForUnsafeMethods]
    serializer_class = StoreUploadSerializer
    queryset = StoreUpload.objects.all()

    def handle_exception(self, exc):
        return format_exception(exc, self.request)