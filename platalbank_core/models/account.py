from django.db import models
from rest_framework import serializers
from rest_framework import viewsets

class Account(models.Model):
    balance = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.CharField(max_length=1024)
    short_name = models.CharField(max_length=128)
    # TODO: owner = models.ForeignKey("LegalPerson")

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

