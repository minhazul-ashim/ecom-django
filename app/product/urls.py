from rest_framework.routers import SimpleRouter
from product.views import ProductViewSet, ProductVariantViewSet, PriceVariantViewSet

router = SimpleRouter()

router.register(r'product', ProductViewSet, basename='products')
router.register(r'product-variant', ProductVariantViewSet, basename='product-variants')
router.register(r'price-variant', PriceVariantViewSet, basename='price-variants')

urlpatterns = router.urls