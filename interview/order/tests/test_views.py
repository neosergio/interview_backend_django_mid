from datetime import datetime

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from ...inventory.models import Inventory, InventoryLanguage, InventoryType
from ..models import Order


class DeactivateOrderViewTest(TestCase):
    def setUp(self):
        # Create a test order for the purpose of testing
        inventory_type = InventoryType.objects.create(name='type1')
        inventory_language = InventoryLanguage.objects.create(name='language1')
        inventory_item = Inventory.objects.create(name='Item 1', type=inventory_type, language=inventory_language,
                                              metadata={'key': 'value'})
        self.order = Order.objects.create(inventory=inventory_item, is_active=True, start_date=datetime.today(), embargo_date=datetime.today())

        # Set up the API client
        self.client = APIClient()

    def test_deactivate_order(self):
        # Get the URL for deactivating the order
        url = reverse('deactivate-order', args=[self.order.id])

        # Make a PATCH request to deactivate the order
        response = self.client.patch(url)

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Refresh the order from the database
        self.order.refresh_from_db()

        # Check if the order is deactivated (is_active set to False)
        self.assertFalse(self.order.is_active)
