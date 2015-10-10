from platalbank_core.models import Event, Transaction, Account

from decimal import Decimal
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
