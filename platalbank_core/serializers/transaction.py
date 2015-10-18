from rest_framework import serializers

from platalbank_core.models import Transaction

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ('url', 'id', 'state', 'amount', 'label', 'debited_account', 'credited_account', 'event','timestamp','last_modified')
