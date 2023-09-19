from datetime import timezone
from itertools import product
from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client

from main.forms import ProductForm

# Create your tests here.
class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

class TestModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        product.objects.create(name="Rhinos", amount=100, price=200000, date_added=timezone.now, description="Obat flu")

    def test_string_method(self):
        product = ProductForm.objects.get(id=1)
        expected_string = f"Name: {product.name} {product.amount} {product.price} {product.date_added} {product.description}"
        self.assertEqual(str(product), expected_string)