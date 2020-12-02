from django.db import models

# Create your models here.
class producto(models.Model):
    descripcion=models.CharField(max_length=30)
    tipo=models.CharField(max_length=40)

    class meta():
        verbose_name='descripcion'
        verbose_name_plural='descripciones'

def __str__(self):
    return self.descripcion

class detalle(models.Model):
    cantidad=models.IntegerField()
    descripcion=models.CharField(max_length=40)
    precio=models.IntegerField()
    forma_pago=models.CharField(max_length=20)
    id_producto=models.OneToOneField(producto,on_delete=models.CASCADE)

    class meta():
        verbose_name='descripcion'
        verbose_name_plural='descripciones'

def __str__(self):
    return self.descripcion

class estado(models.Model):
    descripcion=models.CharField(max_length=30)
    estado=models.CharField(max_length=20)
    id_detalle=models.OneToOneField(detalle,on_delete=models.CASCADE)

    class meta():
        verbose_name='descripcion'
        verbose_name_plural='descripciones'

def __str__(self):
    return self.descripcion

