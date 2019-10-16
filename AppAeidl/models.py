from django.db import models
from AppAeidl.choices import genero_choices


# Create your models here.

class Appointment(models.Model):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return f'{self.name}'


class Medic(models.Model):
    identificacion = models.CharField(max_length=15)
    name = models.CharField(max_length=50)
    user = models.OneToOneField('auth.User', null=True, on_delete=models.SET_NULL)
    telefono = models.CharField(max_length=15)
    genero = models.CharField(max_length=10, choices=genero_choices.CHOICES)
    appointment = models.ForeignKey('Appointment', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.identificacion}, {self.name}'


class Entity(models.Model):
    name = models.CharField(max_length=20, null=False, unique=True)

    def __str__(self):
        return f'{self.name}'


class Patient(models.Model):
    identificacion = models.CharField(max_length=15, null=False, unique=True)
    name = models.CharField(max_length=50, null=False)
    genero = models.CharField(max_length=10, choices=genero_choices.CHOICES,
                              null=False)
    fecha_nac = models.DateField(null=False)
    ocupacion = models.CharField(max_length=30, null=False)
    telefono = models.CharField(max_length=15, null=False, unique=True)
    direccion = models.CharField(max_length=50, null=False)
    entity = models.ForeignKey('Entity', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.identificacion}, {self.name}'


class Study(models.Model):
    name = models.CharField(max_length=80, null=False, unique=True)

    def __str__(self):
        return f'{self.name}'


class Analisi(models.Model):
    patient = models.ForeignKey('Patient', null=False,
                                on_delete=models.CASCADE)
    medic = models.ForeignKey('Medic', null=True,
                              on_delete=models.SET_NULL)
    study = models.ForeignKey('Study', null=True, on_delete=models.SET_NULL)
    fecha = models.DateField(auto_now_add=True, null=True)
    file = models.FileField(null=False)

    def __str__(self):
        return f'Paciente: {self.patient.name}, Medico: {self.medic.name}, ' \
               f'Estudio: {self.study.name}, Fecha: {self.fecha}'



