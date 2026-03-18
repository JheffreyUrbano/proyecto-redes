from django.core.mail import send_mail
from django.conf import settings


def enviar_correo(destinatario, asunto, mensaje):
    try:
        send_mail(
            asunto,
            mensaje,
            settings.EMAIL_HOST_USER,
            [destinatario],
            fail_silently=False,
        )
        return True
    except Exception as e:
        print("ERROR EMAIL:", e)
        return False
