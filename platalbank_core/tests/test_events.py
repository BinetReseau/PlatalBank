from platalbank_core.models import Event, Transaction, Account

from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class EventTests(APITestCase):
    @classmethod
    def setUpTestData(self):
        super(EventTests, self).setUpTestData()

        self.event, _ = Event.objects.get_or_create(label='Test', through_khube=True, writable=True)
    
    def test_event_close(self):
        self.assertEqual(Event.objects.get(id=1).writable, True)
        url = reverse('event-close',args=[1])
        data = {}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Event.objects.get(id=1).writable, False)

    def test_event_not_found(self):
        url = reverse('event-close',args=[2])
        data = {}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
