from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Order, Product, OrderProduct
import datetime

# Create your tests here.


class ProductModelTest(TestCase):
    """Tests for the Product model."""


    def setUp(self):
        product = Product.objects.create(
            name="product1",
            price=10.5,
        )

    def test_product_creation(self):
        products = Product.objects.all()
        self.assertEqual(products.count(), 1)
        self.assertEqual(products[0].name, "product1")
        self.assertEqual(products[0].price, 10.5)



class OrderModelTest(TestCase):
    """Tests for the Product model."""


    def setUp(self):
        product = Product.objects.create(
            name="product1",
            price=10.5,
        )
        order = Order.objects.create(name="order1", description="order_desc1", date="2025-01-01")
        order_product = OrderProduct.objects.create(order=order, product=product, quantity=2)

    def test_order_creation(self):
        orders = Order.objects.all()
        self.assertEqual(orders.count(), 1)
        self.assertEqual(orders[0].name, "order1")
        self.assertEqual(orders[0].date, datetime.date(2025, 1, 1))
        self.assertEqual(orders[0].orderproduct_set.all()[0].product.name, "product1")
        self.assertEqual(orders[0].orderproduct_set.all().count(), 1)
        self.assertEqual(orders[0].orderproduct_set.all()[0].quantity, 2)
    



class ProductAPITests(APITestCase):
    def setUp(self):

        self.product = Product.objects.create(name="product1", price=10.0)    
        self.url = '/api/products/'
        self.detail_url = f'/api/products/{self.product.id}/'
    
    def test_detail_product(self):
        
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'id': 1, 'name': 'product1', 'price': '10.00'})

    def test_list_products(self):
        
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_product_creation(self):  
        data = {'name': 'product2', 'price': 20.0}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)
        self.assertEqual(Product.objects.get(id=2).name, 'product2')
        self.assertEqual(Product.objects.get(id=2).price, 20.0)
    

    def test_product_update(self):  
        data = {'name': 'updated_product', 'price': 15.0}
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.name, 'updated_product')
        self.assertEqual(self.product.price, 15.0)





class OrderAPITests(APITestCase):
    def setUp(self):

        self.product = Product.objects.create(name="product1", price=10.00)
        self.order = Order.objects.create(name="order1", description="order_desc1", date="2025-01-01")
        self.order_product = OrderProduct.objects.create(order=self.order, product=self.product, quantity=2)
        

        self.list_url = '/api/orders/'
        self.detail_url = f'/api/orders/{self.order.id}/'

    def test_detail_order(self):
        """Ensure we can retrieve an order detail."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = {
            'id': self.order.id,
            'name': self.order.name,
            'description': self.order.description,
            'date': str(self.order.date),
            'items': [
                {
                    'product': self.product.id,
                    'product_name': self.product.name,
                    'product_price': str(self.product.price),
                    'quantity': self.order_product.quantity
                }
            ]
        }
        self.assertEqual(response.data['id'], expected_data['id'])
        self.assertEqual(response.data['date'], expected_data['date'])
        self.assertEqual(len(response.data['items']), 1)
    
    # def test_forbid_order_creation(self):
    #     data = {'name': 'NewOrder', 'description': 'description'}
    #     response = self.client.post(self.list_url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)
        

    def test_filter_order_by_date(self):

        response = self.client.get(f'{self.list_url}?date=2025-01-01')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


    def test_search_order_by_name(self):
        response = self.client.get(f'{self.list_url}?search=order1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


    def test_search_order_by_description(self):
        response = self.client.get(f'{self.list_url}?search=order_desc1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        
    def test_order_update(self):
        updated_data = {'description': 'edited_description'}
        response = self.client.patch(self.detail_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], 'edited_description')
        





