from django.db import models


class EmailLog(models.Model):
    destinatario = models.EmailField()
    asunto = models.CharField(max_length=255)
    mensaje = models.TextField()
    enviado = models.BooleanField(default=False)
    fecha_envio = models.DateTimeField(auto_now_add=True)
    error = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'email_log'

    def __str__(self):
        return f"{self.destinatario} - {self.asunto}"
