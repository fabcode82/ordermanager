from django.contrib import admin

# Register your models here.


from orders.models import Product, Order, OrderProduct

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderProduct)
