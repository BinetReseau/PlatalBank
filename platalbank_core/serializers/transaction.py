from rest_framework import serializers

from platalbank_core.models import Transaction

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.SerializerMethodField()
    def get_author(self, obj):
        return 'Dummy'

    class Meta:
        model = Transaction
        fields = ('url', 'id', 'state', 'amount', 'label', 'debited_account', 'credited_account', 'event','timestamp','last_modified','author')
