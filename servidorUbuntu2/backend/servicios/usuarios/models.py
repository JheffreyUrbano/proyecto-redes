from django.db import models


class Area(models.Model):
    codarea = models.CharField(primary_key=True, max_length=2)
    descripcion = models.CharField(max_length=150)
    estado = models.BooleanField()

    class Meta:
        db_table = 'area'


class Usuario(models.Model):
    codusuario = models.CharField(primary_key=True, max_length=5)
    nombre = models.CharField(max_length=200)
    cargo = models.CharField(max_length=100)

    login = models.CharField(max_length=50)
    password = models.CharField(db_column='pass', max_length=50)

    email = models.EmailField()
    estado = models.BooleanField()

    codperfil = models.CharField(max_length=2)

    class Meta:
        db_table = 'usuario'
