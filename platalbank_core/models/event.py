from django.db import models

class Event(models.Models)
    label = models.CharField(max_length=1024)
    # if true, authorization requests will be sent to the khube, otherwise to the customer.
    through_khube = models.BooleanField()
    # whether new transactions can be added
    writable = models.BooleanField()


