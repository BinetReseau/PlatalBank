from django.db import models

class Account(models.Model):
    balance = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.CharField(max_length=100)
    short_name = models.CharField(max_length=4)
    #todo : owner
