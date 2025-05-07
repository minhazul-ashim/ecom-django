from rest_framework import routers
from subcategory.views import SubcategoryViewSet

router = routers.SimpleRouter()

router.register(r'subcategory', SubcategoryViewSet)

urlpatterns = router.urls