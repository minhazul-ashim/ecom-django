from django.shortcuts import render
from rest_framework import viewsets
from app.permissions import IsAdminForUnsafeMethods
from product.serializers import ProductSerializer
from product.models import Product
from app.utils import format_exception

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminForUnsafeMethods]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        queryset = Product.objects.select_related('category_id', 'subcategory_id').all()
        return queryset
    
    def handle_exception(self, exc):
        return format_exception(exc, self.request)