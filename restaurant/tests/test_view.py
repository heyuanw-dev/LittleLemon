from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        item1 = MenuItem.objects.create(title="Pizza", price=10.99, inventory=5)
        item2 = MenuItem.objects.create(title="Burger", price=7.49, inventory=10)
        item3 = MenuItem.objects.create(title='Salad', price=5.99, inventory=8)

    def test_getall(self):
        response = self.client.get(reverse("menu-items"))
        menu = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
        
