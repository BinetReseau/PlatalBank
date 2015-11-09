from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from django.http import HttpResponse

from platalbank_core.models import Event
from platalbank_core.serializers import EventSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    @detail_route(methods=["post"])
    def close(self, request , pk=None):
    	try:
    		event = Event.objects.get(id=pk)
    	except Event.DoesNotExist:
    		HttpResponse(status=404)

    	#On prevoit l'emplacement logique pour une verification de la permission
    	if True:
    		event.writable = False
    		event.save()
    		return Response({'status':'Event closed'})
    	else :
    		raise exceptions.PermissionDenied