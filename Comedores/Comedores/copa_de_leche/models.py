from django.db import models

# Create your models here.

class escuela(models.Model):
    establecimiento = models.CharField(max_length=60)
    cue = models.CharField(max_length=9)
    delegacion = models.CharField(max_length=30)
    localidad = models.CharField(max_length=30)
    nivel = models.CharField(max_length=20)
    modalidad = models.CharField(max_length=20)
    nro_cuenta = models.CharField(max_length=8)
    responsable = models.CharField(max_length=30)
    responsable_dni = models.CharField(max_length=10)
    sub_responsable = models.CharField(max_length=30, blank=True, null=True)
    sub_responsable_dni = models.CharField(max_length=10)
    reso = models.CharField(max_length=6, blank=True, null=True)
