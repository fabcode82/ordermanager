# serializers.py
from .models import (
    Order,
    Product,
    OrderProduct,
)
from rest_framework import serializers
from django.db import transaction # per transazioni atomiche





class ProductSerializer(serializers.ModelSerializer):


    class Meta:
        model = Product
        fields = ["id", "name", "price", ]






# --- OrderProduct Serializers (Nested) ---
class OrderProductDisplaySerializer(serializers.ModelSerializer):
    """
    Display OrderProduct details (GET ).
    Includes nested product information.
    """

    product_id = serializers.ReadOnlyField(source='product.id')
    product_name = serializers.ReadOnlyField(source='product.name')
    product_price = serializers.ReadOnlyField(source='product.price')

    class Meta:
        model = OrderProduct

        fields = ['id', 'product_id', 'product_name', 'product_price', 'quantity']


class OrderProductCreationSerializer(serializers.ModelSerializer):
    """
    Create OrderProduct instances (POST/PUT/PATCH ).
    for product we need ID and quantity.
    """
    class Meta:
        model = OrderProduct
        # The user only sends 'product' (ID) and 'quantity'
        fields = ['product', 'quantity']


# --- Order Serializer ---
class OrderSerializer(serializers.ModelSerializer):
    """
    Order model serializer , with nested OrderProduct items
    read and write.
    """
    
    # Field for display (GET), we user display serializer
    items = OrderProductDisplaySerializer(
        source='orderproduct_set',  
        many=True, 
        read_only=True
    )
    
    # Field for input (POST PUT PATCH): we uses the creation serializer
    items_in = OrderProductCreationSerializer(
        many=True, 
        write_only=True,
        required=False # Allow orders without items
    )

    class Meta:
        model = Order
        fields = ['id', 'name', 'description', 'date', 'created_at', 'updated_at', 'items', 'items_in']
        read_only_fields = ['created_at', 'updated_at']

    # override CREATE method for nested OrderProduct objects
    @transaction.atomic 
    def create(self, validated_data):
        """Creates an Order and its related OrderProduct ."""
        

        items_data = validated_data.pop('items_in', [])
        

        order = Order.objects.create(**validated_data)

        # Create the OrderProduct 
        for item_data in items_data:
            # item_data['product'] is already an instance
            OrderProduct.objects.create(order=order, **item_data)

        return order

    # override UPDATE  to manage nested OrderProduct 
    @transaction.atomic 
    def update(self, instance, validated_data):
        """
        Updates an  Order and manages and its nested OrderProducts .
        
        destructive approach on old OrderProducts, delete all and recreate.
        """
        
        # Aggiorno oggetto Order
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        

        if 'items_in' in validated_data:
            items_data = validated_data.pop('items_in')

            # replace old OrderProducts
            instance.orderproduct_set.all().delete()
            
            # create all OrderProducts
            for item_data in items_data:
                OrderProduct.objects.create(order=instance, **item_data)
        
        return instance

