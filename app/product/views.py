from rest_framework import viewsets
from app.permissions import IsAdminForUnsafeMethods
from product.serializers import PriceVariantSerializer, ProductSerializer, ProductVariantSerializer
from product.models import Product, PriceVariant, ProductVariant
from app.utils import format_exception

#------------------------Product Views-------------------------------
class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminForUnsafeMethods]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_queryset(self):
        queryset = Product.objects.select_related('category_id', 'subcategory_id').all()
        return queryset
    
    def handle_exception(self, exc):
        return format_exception(exc, self.request)


#------------------------Product Variant Views-------------------------------
class ProductVariantViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminForUnsafeMethods]
    serializer_class = ProductVariantSerializer
    queryset = ProductVariant.objects.all()

    def get_queryset(self):
        queryset = ProductVariant.objects.all()
        return queryset
    
    def handle_exception(self, exc):
        return format_exception(exc, self.request)


#------------------------Price Variant Views-------------------------------
class PriceVariantViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminForUnsafeMethods]
    serializer_class = PriceVariantSerializer
    queryset = PriceVariant.objects.all()

    def get_queryset(self):
        queryset = PriceVariant.objects.all()
        return queryset
    
    def handle_exception(self, exc):
        return format_exception(exc, self.request)