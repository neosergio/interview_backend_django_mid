from rest_framework.test import APITestCase
from rest_framework import status
from ..models import Inventory, InventoryTag, InventoryType, InventoryLanguage
from django.urls import reverse

class InventoryItemListAfterDateTest(APITestCase):
    def setUp(self):
        # Create some test data
        inventory_type = InventoryType.objects.create(name='type1')
        inventory_language = InventoryLanguage.objects.create(name='language1')
        self.item1 = Inventory.objects.create(name='Item 1', type=inventory_type, language=inventory_language, metadata={'key':'value'})
        self.item2 = Inventory.objects.create(name='Item 2', type=inventory_type, language=inventory_language,
                                              metadata={'key': 'value'})
        self.item3 = Inventory.objects.create(name='Item 3', type=inventory_type, language=inventory_language,
                                              metadata={'key': 'value'})

    def test_list_inventory_items_after_date(self):
        # Format the date string to match the format in the URL
        created_at_date = self.item1.created_at.strftime('%Y-%m-%d')

        # Make a GET request to the API endpoint
        url = reverse('inventory-list-created-after-date', args=[created_at_date])
        response = self.client.get(url)

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the correct number of items is returned
        self.assertEqual(len(response.data), 3)

    def test_invalid_date_format(self):
        # Make a GET request with an invalid date format
        url = reverse('inventory-list-created-after-date', args=['invalid_date'])
        response = self.client.get(url)

        # Check if the response status code is 400 Bad Request
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
