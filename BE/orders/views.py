
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework import viewsets
from rest_framework import mixins  
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Product, Order
from .serializers import (
    ProductSerializer,
    OrderSerializer
)



class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()  
    serializer_class = ProductSerializer  


class OrderModelViewSet(ModelViewSet):
    queryset = Order.objects.all().prefetch_related('orderproduct_set') 
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['date'] 
    search_fields = ['name', 'description']
    # .../api/orders/?search=order1
    # .../api/orders/?date=2025-10-17



# # TO DISABLE CREATION OF ORDERS VIA API
# class OrderViewSet(
#     mixins.ListModelMixin,      
#     mixins.RetrieveModelMixin,   
#     mixins.UpdateModelMixin,   
#     mixins.DestroyModelMixin, 
#     viewsets.GenericViewSet
# ):
#     """
#     version to forbid creation of orders via api
#     """

#     queryset = Order.objects.all().prefetch_related('orderproduct_set') 
#     serializer_class = OrderSerializer


#     filter_backends = [DjangoFilterBackend, SearchFilter]
#     filterset_fields = ['date'] 
#     search_fields = ['name', 'description']
#     # .../api/orders/?search=order1
#     # .../api/orders/?date=2025-10-17



