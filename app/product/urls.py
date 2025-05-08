from rest_framework.routers import SimpleRouter
from product.views import ProductViewSet

router = SimpleRouter()

router.register(r'product', ProductViewSet, basename='products')

urlpatterns = router.urls