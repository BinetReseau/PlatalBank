from rest_framework.response import Response
from rest_framework import viewsets , exceptions , decorators

from platalbank_core.models import Transaction
from platalbank_core.serializers import TransactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    @decorators.detail_route(methods="post")
    def setState(self, request, pk=None):

        try :
            transaction = Transaction.object.get(id=pk)
        except Transaction.doesNotExist:
            return HttpResponse(status=404)

        #Une fois les permissions implementees, ce type de changement d'etat demandera des permissions Khube ou User
        if (request.state in [Transaction.AUTHORIZED , Transaction.REJECTED]):
            transaction.state = Transaction._STATE_CHOICES(request.state)
            transaction.save()

            return Response({'status':'Transaction {0}'.format(Tansaction._STATE_CHOICES(request.state))})

        #Ce type de changement d'etat demandera des permissions seller
        elif (request.state in [Transaction.ABORTED,Transaction.COMPLETED]):
            transaction.state = Transaction._STATE_CHOICES(request.state)

            transaction.save()

            return Response({'status':'Transaction {0}'.format(Tansaction._STATE_CHOICES(request.state))})

        else :
            return exceptions.PermissionDenied()