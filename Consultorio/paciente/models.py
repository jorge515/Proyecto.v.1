from django.db import models

# Create your models here.
class Paciente(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    historia=models.TextField("Historial")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='Paciente'
        verbose_name_plural='pacientes'

def __str__ (self):
    return self.nombre
    


class Medico(models.Model):
    nombre=models.TextField(max_length=30)
    apellido=models.TextField()

    class Meta:
        verbose_name='medico '
        verbose_name_plural='medicos'

def __str__(self):
    return self.nombre

class Historial(models.Model):
    pacient=models.OneToOneField(Paciente,verbose_name="Paciente", on_delete=models.CASCADE)
    medico=models.OneToOneField(Medico, on_delete=models.CASCADE)
    descripcion=models.TextField(max_length=30)

    class Meta:
        verbose_name='historial'
        verbose_name_plural='historial'

def __str__(self):
    return self.paciente


class Turno(models.Model):
    dia=models.DateField()
    hora=models.TimeField()
    paciente=models.OneToOneField(Paciente, on_delete=models.CASCADE)
    medico=models.ForeignKey(Medico, on_delete=models.CASCADE)

    class Meta:
        verbose_name='turno'
        verbose_name_plural='turnos'

def __str__(self):
    return self.dia

class Estado(models.Model):
    estado=models.CharField(max_length=30)
    turno=models.OneToOneField(Turno, on_delete=models.CASCADE)

    class Meta:
        verbose_name='estado'
        verbose_name_plural='estados'

def __str__(self):
    return self.estado
