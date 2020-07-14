from django.db import models

class expediente(models.Model):
    fecha_inicio=models.DateTimeField(auto_now=True)
    descripcion=models.CharField(max_length=150)
    nota_nro=models.CharField(max_length=6)
    mesa_entra_uppe=models.DateTimeField()
    delegacion=models.CharField()
    mes=models.CharField()
    monto=models.FloatField()
    mesa_entra_min=models.DateField()
    expediente=models.CharField(10)
    reso=models.CharField(10)

    def __str__(self):
        return (self.nota_nro, self.descripcion, self.fecha_inicio,
        self.descripcion, self.delegacion, self.expediente)

