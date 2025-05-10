from rest_framework.routers import SimpleRouter
from settings.views import *

router = SimpleRouter()

router.register(r'attribute', AttributeViewset, basename='attribute')
router.register(r'attribute-item', AttributeItemViewset, basename='attribute-item')
router.register(r'unit', UnitTypeViewset, basename='unit-type')
router.register(r'store', StoreInfoViewset, basename='store-info')
router.register(r'social', SocialMediaViewset, basename='social-media')
router.register(r'page', ExtraPageViewset, basename='extra-page')
router.register(r'store-gallery', StoreGalleryViewset, basename='store-gallery')
router.register(r'store-upload', StoreUploadViewset, basename='store-upload')


urlpatterns = router.urls