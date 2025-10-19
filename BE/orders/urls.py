from rest_framework.routers import DefaultRouter
from .views import (ProductModelViewSet, 
                    OrderModelViewSet, 

)

router = DefaultRouter()
router.register(r'products', ProductModelViewSet, basename='product')
router.register(r'orders', OrderModelViewSet, basename='order')


urlpatterns = router.urls



