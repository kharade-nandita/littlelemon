from django.test import TestCase
from restaurant.models import Menu, Booking
from datetime import datetime


class MenuModelTest(TestCase):
    def test_menu_creation(self):
        item = Menu.objects.create(title="Lemon Cake", price="8.50", inventory=10)
        self.assertEqual(str(item), "Lemon Cake")


class BookingModelTest(TestCase):
    def test_booking_creation(self):
        booking = Booking.objects.create(
            name="Test Guest",
            no_of_guests=2,
            booking_date=datetime(2026, 10, 24, 18, 0)
        )
        self.assertEqual(str(booking), "Test Guest")
