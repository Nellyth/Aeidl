from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models
from AppAeidl.choices import GenderChoices, StatusChoices
from AppAeidl.utils.Validations import positive_integer_field


# Create your models here.
class Company(models.Model):
    nit = models.CharField(unique=True, validators=[positive_integer_field], max_length=10)
    name = models.CharField(unique=True, max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(unique=True, validators=[positive_integer_field], max_length=12)

    def __str__(self):
        return f'{self.nit} - {self.name}'


class Person(AbstractUser):
    identification = models.CharField(unique=True, max_length=10, validators=[positive_integer_field])
    gender = models.TextField(choices=GenderChoices.CHOICES, max_length=20)
    phone = models.CharField(unique=True, max_length=12, validators=[positive_integer_field])

    def __str__(self):
        return f'{self.identification} - {self.get_username()}'

    class Meta(AbstractUser.Meta):
        swappable = 'AppAeidl.Person'


class Entity(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f'{self.name}'


class Patient(models.Model):
    date_birth = models.DateField()
    direction = models.CharField(max_length=150)
    person = models.OneToOneField('Person', on_delete=models.CASCADE)
    entity = models.ForeignKey('Entity', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.person.identification}, {self.person.get_username()}'


class Specialty(models.Model):
    name = models.CharField(max_length=150)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        unique_together = (('name', 'company'),)


class Role(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        unique_together = (('name', 'company'),)


class Medic(models.Model):
    role = models.ForeignKey('Role', null=True, on_delete=models.SET_NULL)
    specialty = models.ForeignKey('Specialty', null=True, on_delete=models.SET_NULL)
    person = models.OneToOneField('Person', on_delete=models.CASCADE)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.person.identification}, {self.person.get_username()}'


class Study(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey('Company', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        unique_together = (('name', 'company'),)


class Exam(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    medic = models.ForeignKey('Medic', null=True, on_delete=models.SET_NULL)
    study = models.ForeignKey('Study', null=True, on_delete=models.SET_NULL)
    date = models.DateField(auto_now_add=True, null=True)
    status = models.CharField(choices=StatusChoices.CHOICES, max_length=40)
    file = models.FileField()
    result = models.TextField(max_length=500)

    def __str__(self):
        return f'Patient: {self.patient.person.identification}, Medic: {self.medic.person.identification}, ' \
               f'Study: {self.study.name}, Date: {self.date}'
