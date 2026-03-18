# servicios/requisiciones/models.py

from django.db import models
from django.utils import timezone


#requisición
class Requisicion(models.Model):
    requino = models.CharField(primary_key=True, max_length=20)
    fecha = models.CharField(max_length=10)
    obs = models.CharField(max_length=254)
    valor_total = models.FloatField()

    codusuario = models.CharField(max_length=20)
    codestado = models.CharField(max_length=2)
    codproveedor = models.CharField(max_length=20)

    class Meta:
        db_table = 'requisicion'
        managed = False

    def __str__(self):
        return self.requino

# detalle_requisicion
class DetalleRequisicion(models.Model):
    item = models.FloatField(primary_key=True)

    requisicion = models.ForeignKey(
        Requisicion,
        on_delete=models.CASCADE,
        db_column='requino',
        related_name='detalles'
    )

    producto = models.ForeignKey(
        'productos.Producto',
        on_delete=models.PROTECT,
        db_column='codproducto'
    )

    cantidad = models.FloatField()
    valor = models.FloatField()

    class Meta:
        db_table = 'detalle_requisicion'
        managed = False

    def __str__(self):
        return f"{self.requisicion_id} - {self.producto_id}"


# log_requisicion
class LogRequisicion(models.Model):
    id = models.AutoField(primary_key=True)

    requisicion = models.ForeignKey(
        Requisicion,
        on_delete=models.CASCADE,
        db_column='requino'
    )

    codusuario = models.CharField(max_length=20)
    accion = models.CharField(max_length=20)

    fecha = models.DateTimeField(default=timezone.now)

    ip_address = models.CharField(max_length=45, null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)

    codestado_anterior = models.CharField(max_length=2, null=True, blank=True)
    codestado_nuevo = models.CharField(max_length=2, null=True, blank=True)

    observaciones = models.CharField(max_length=500, null=True, blank=True)
    datos_modificados = models.JSONField(null=True, blank=True)

    class Meta:
        db_table = 'log_requisicion'
        managed = False
