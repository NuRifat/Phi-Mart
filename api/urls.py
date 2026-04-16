from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from product.views import ProductViewSet, CategoryViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)

# urlpatterns = router.urls

# For multiple urls path:
urlpatterns = [
    path('',include(router.urls)),
]


# urlpatterns = [
#     path('products/', include('product.product_urls')),
#     path('categories/', include('product.category_urls')),
# ]