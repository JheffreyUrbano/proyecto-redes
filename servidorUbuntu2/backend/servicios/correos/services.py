from django.core.mail import send_mail
from django.conf import settings


def enviar_correo(destinatario, asunto, mensaje, estado):
    cuerpo = f"""
Estado de la requisición: {estado}

{mensaje}
"""

    try:
        send_mail(
            subject=asunto,
            message=cuerpo,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[destinatario],
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(e)
        return False
