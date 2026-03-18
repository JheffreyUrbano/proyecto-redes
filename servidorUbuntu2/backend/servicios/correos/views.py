from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .services import enviar_correo


@api_view(['POST'])
def enviar_email(request):
    destinatario = request.data.get('destinatario')
    asunto = request.data.get('asunto')
    mensaje = request.data.get('mensaje')
    estado = request.data.get('estado')

    if not all([destinatario, asunto, mensaje, estado]):
        return Response(
            {"error": "Faltan datos"},
            status=status.HTTP_400_BAD_REQUEST
        )

    ok = enviar_correo(destinatario, asunto, mensaje, estado)

    return Response({"enviado": ok})
