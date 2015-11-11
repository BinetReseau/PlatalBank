from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import exceptions
from rest_framework.decorators import detail_route
from django.http import HttpResponse

from platalbank_core.models import Transaction
from platalbank_core.serializers import TransactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    @detail_route(methods=['post'])
    def setState(self, request, pk=None):

        try :
            transaction = Transaction.objects.get(id=pk)
        except Transaction.DoesNotExist:
            return HttpResponse(status=404)

        state = request.data.get('state')

        #Une fois les permissions implementees, ce type de changement d'etat demandera des permissions Khube ou User
        if (state in [Transaction.AUTHORIZED , Transaction.REJECTED]):
            transaction.state = state
            transaction.save()

            return Response({'status':'State modified'})

        #Ce type de changement d'etat demandera des permissions seller
        elif (state in [Transaction.ABORTED,Transaction.COMPLETED]):
            transaction.state = state
            transaction.save()

            return Response({'status':'State modified'})

        else :
            raise exceptions.PermissionDenied
