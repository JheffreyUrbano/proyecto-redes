# servicios/productos/models.py

from django.db import models


class Proveedor(models.Model):
    codproveedor = models.CharField(primary_key=True, max_length=20)
    descripcion = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=20)
    estado = models.BooleanField()

    class Meta:
        db_table = 'proveedor'
        managed = False

    def __str__(self):
        return self.descripcion


class Producto(models.Model):
    codproducto = models.CharField(primary_key=True, max_length=20)
    descripcion = models.CharField(max_length=150)
    precio = models.FloatField()
    cantidad = models.FloatField()
    cmi = models.FloatField()
    estado = models.BooleanField()

    class Meta:
        db_table = 'producto'
        managed = False

    def __str__(self):
        return self.descripcion
