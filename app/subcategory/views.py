from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app.permissions import IsAdminForUnsafeMethods
from subcategory.models import Subcategory
from subcategory.serializers import SubcategorySerializer
from app.utils import format_exception

# Create your views here.
class SubcategoryViewSet(ModelViewSet):
    permission_classes = [IsAdminForUnsafeMethods]
    serializer_class = SubcategorySerializer
    queryset = Subcategory.objects.all()

    def get_queryset(self):
        queryset = Subcategory.objects.select_related('category').all()
        return queryset
    
    # def get_serializer_class(self):
    #     if (self.action in ['list', 'retrieve']):
    #         return SubcategorySerializer

    def handle_exception(self, exc):
        return format_exception(exc, self.request)