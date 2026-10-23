from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from restaurant.models import Menu


class HomeViewTest(TestCase):
    def test_homepage(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to Little Lemon")


class MenuAPITest(TestCase):
    def test_menu_endpoint(self):
        Menu.objects.create(title="Lemon Cake", price="8.50", inventory=10)
        response = APIClient().get("/api/menu/")
        self.assertEqual(response.status_code, 200)
