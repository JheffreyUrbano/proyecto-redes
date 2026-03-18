from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Usuario


@api_view(['POST'])
def login(request):
    login = request.data.get("login")
    password = request.data.get("password")

    try:
        user = Usuario.objects.get(login=login, password=password)

        return Response({
            "codusuario": user.codusuario,
            "nombre": user.nombre,
            "perfil": user.codperfil
        })

    except Usuario.DoesNotExist:
        return Response({"error": "Credenciales inválidas"}, status=401)
