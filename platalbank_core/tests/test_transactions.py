from platalbank_core.models import Event, Transaction, Account

from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

def reload(obj):
    return obj.__class__.objects.get(pk=obj.pk)

class TransactionTests(APITestCase):
    @classmethod
    def setUpTestData(self):
        super(TransactionTests, self).setUpTestData()

        self.event, _ = Event.objects.get_or_create(label='Test', through_khube=True, writable=True)
        self.accA, _ = Account.objects.get_or_create(short_name='A', balance=4200)
        self.accB, _ = Account.objects.get_or_create(short_name='B', balance=1337)

    def test_transaction(self):
        self.accA, self.accB = reload(self.accA), reload(self.accB)
        self.assertEqual(self.accA.balance, 4200)
        self.assertEqual(self.accB.balance, 1337)
        Transaction.objects.create(
            amount=500,
            label='Test',
            debited_account=self.accA,
            credited_account=self.accB,
            event=self.event
        )
        self.accA, self.accB = reload(self.accA), reload(self.accB)
        self.assertEqual(self.accA.balance, 3700)
        self.assertEqual(self.accB.balance, 1837)

    # Test what happens when save is called twice
    def test_not_duplicate_transfer(self):
        self.accA, self.accB = reload(self.accA), reload(self.accB)
        self.assertEqual(self.accA.balance, 4200)
        self.assertEqual(self.accB.balance, 1337)
        Transaction.objects.create(
            amount=500,
            label='Test',
            debited_account=self.accA,
            credited_account=self.accB,
            event=self.event
        )
        self.accA, self.accB = reload(self.accA), reload(self.accB)
        self.assertEqual(self.accA.balance, 3700)
        self.assertEqual(self.accB.balance, 1837)

    def test_transaction_setState(self):
        Transaction.objects.create(
            amount=500,
            label='Test',
            debited_account=self.accA,
            credited_account=self.accB,
            event=self.event
        )
        self.assertEqual(Transaction.objects.get(id=1).state, 'P')
        url = reverse('transaction-setState',args=[1])
        data = {'state': 'C'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Transaction.objects.get(id=1).state, 'C')
