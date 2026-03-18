from servicios.notificaciones.models import Notificacion
from servicios.correos.models import Correo
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone

from .models import Requisicion, Funciones, Usuario, LogRequisicion
from .models import Asignacion, Funciones, Usuario


def registrar_log(requisicion, usuario, accion, estado_anterior, estado_nuevo, request=None):

    LogRequisicion.objects.create(
        requino=requisicion,
        codusuario=usuario,
        accion=accion,
        fecha=timezone.now(),
        ip_address=request.META.get('REMOTE_ADDR') if request else None,
        user_agent=request.META.get('HTTP_USER_AGENT') if request else None,
        codestado_anterior=estado_anterior,
        codestado_nuevo=estado_nuevo,
        observaciones=f"Cambio de estado: {accion}"
    )


def enviar_correo(destinatario, asunto, mensaje):

    correo = Correo.objects.create(
        destinatario=destinatario,
        asunto=asunto,
        mensaje=mensaje
    )

    try:
        send_mail(
            subject=asunto,
            message=mensaje,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[destinatario],
            fail_silently=False,
        )

        correo.enviado = True
        correo.save()

    except Exception as e:
        print("Error enviando correo:", e)


#1. Cuando se crea requisición
def notificar_revisor(requisicion):

    # función = REVISAR (03)
    funcion_revisor = Funciones.objects.get(codfuncion="03")

    # buscar usuarios asignados a esa función
    asignaciones = Asignacion.objects.filter(codfuncion=funcion_revisor)

    for asignacion in asignaciones:

        usuario_revisor = asignacion.codusuario

        mensaje = f"Tienes una requisición pendiente #{requisicion.requino}"

        Notificacion.objects.create(
            usuario=usuario_revisor.nombre,
            mensaje=mensaje
        )

        enviar_correo(
            usuario_revisor.email,
            "Nueva requisición pendiente",
            mensaje
        )

#2. Estado de revisión
def notificar_revision(requisicion):

    usuario = requisicion.codusuario

    mensaje = f"Tu requisición {requisicion.requino} ha sido revisada"

    enviar_correo(
        usuario.email,
        "Requisición revisada",
        mensaje
    )


#3. Estado de autorización
def notificar_autorizador(requisicion):

    funcion_autorizador = Funciones.objects.get(codfuncion="04")

    asignaciones = Asignacion.objects.filter(codfuncion=funcion_autorizador)

    for asignacion in asignaciones:

        usuario = asignacion.codusuario

        mensaje = f"La requisición #{requisicion.requino} está lista para autorización"

        enviar_correo(
            usuario.email,
            "Requisición pendiente de autorización",
            mensaje
        )

#4. Notificar solicitante
def notificar_autorizacion(requisicion):

    usuario = requisicion.codusuario

    mensaje = f"Tu requisición {requisicion.requino} ha sido autorizada"

    enviar_correo(
        usuario.email,
        "Requisición autorizada",
        mensaje
    )

#5. NOtificar Oden de compra
def notificar_oc(requisicion):

    usuario = requisicion.codusuario

    mensaje = f"Se generó la orden de compra para tu requisición {requisicion.requino}"

    enviar_correo(
        usuario.email,
        "Orden de compra generada",
        mensaje
    )
