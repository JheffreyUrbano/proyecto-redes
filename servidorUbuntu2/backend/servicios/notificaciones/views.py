from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import enviar_correo


@api_view(['POST'])
def enviar_email(request):
    destinatario = request.data.get('destinatario')
    asunto = request.data.get('asunto')
    mensaje = request.data.get('mensaje')

    if not destinatario or not asunto or not mensaje:
        return Response({"error": "Faltan datos"}, status=400)

    ok = enviar_correo(destinatario, asunto, mensaje)

    return Response({"enviado": ok})
