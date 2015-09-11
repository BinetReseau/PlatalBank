from django.db import models
from rest_framework import serializers, viewsets

class Event(models.Model):
    label = models.CharField(max_length=1024)
    # if true, authorization requests will be sent to the khube, otherwise to the customer.
    through_khube = models.BooleanField()
    # whether new transactions can be added
    writable = models.BooleanField()
    # TODO: owner = models.ForeignKey("LegalPerson")

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
