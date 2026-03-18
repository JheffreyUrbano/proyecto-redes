from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Requisicion


@api_view(['GET'])
def dashboard(request):
    return Response({
        "total": Requisicion.objects.count(),
        "pendientes": Requisicion.objects.filter(codestado="01").count(),
        "revisadas": Requisicion.objects.filter(codestado="02").count(),
        "autorizadas": Requisicion.objects.filter(codestado="03").count(),
        "oc": Requisicion.objects.filter(codestado="03").count(),
    })
