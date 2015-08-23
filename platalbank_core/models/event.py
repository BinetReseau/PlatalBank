from django.db import models

class Event(models.Models)
    label = models.CharField(max_length=100)
    through_khube = models.BooleanField()#if true, one can seek the khube's authorization
    writable = models.BooleanField() #if false, new transactions cannot be added


