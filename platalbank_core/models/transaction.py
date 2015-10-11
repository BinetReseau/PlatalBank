from django.db import models
from django.conf import settings
from rest_framework import serializers, viewsets

class Transaction(models.Model):
    # when the transaction has been freshly created. No-one has accepted/rejected it yet.
    PENDING = "P"
    # when the khube/the customer has acknowledged the transaction ; it still needs to be completed by the seller.
    AUTHORIZED = "A"
    # when the khube/the customer has rejected the trasaction ; it still needs to be aborted by the seller.
    REJECTED = "R"
    # when the seller has decided not to go on with the transaction ; it only appears in specialized history.
    ABORTED = "X"
    # when the seller has decided to cash in.
    COMPLETED = "C"
    _STATE_CHOICES = (
        (PENDING, "PENDING"),
        (AUTHORIZED, "AUTHORIZED"),
        (REJECTED, "REJECTED"),
        (ABORTED, "ABORTED"),
        (COMPLETED, "COMPLETED"),
    )

    state = models.CharField(max_length=1, choices=_STATE_CHOICES,default=PENDING)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    label = models.CharField(max_length=1024)

    debited_account = models.ForeignKey("Account", related_name="out_transactions")
    credited_account = models.ForeignKey("Account", related_name="in_transactions")
    event = models.ForeignKey("Event")

    # TODO: author = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.label

class TransactionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ('url', 'id', 'state', 'amount', 'label', 'debited_account', 'credited_account', 'event')

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
