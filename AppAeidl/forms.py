from django.forms import ModelForm
from django import forms

from AppAeidl.choices import GenderChoices, StatusChoices
from AppAeidl.models import Medic, Patient, Person, Company, Entity, Specialty, Role, Study, Exam
from datetime import date


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = [
            'identification',
            'first_name',
            'last_name',
            'email',
            'gender',
            'phone',
            'photo'
        ]
        labels = {
            'identification': 'Identification',
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'Email',
            'gender': 'Gender',
            'phone': 'Phone',
            'photo': 'Photo'
        }

        widgets = {
            'identification': forms.NumberInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(choices=GenderChoices.CHOICES, attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'})
        }


class MedicForm(ModelForm):
    class Meta:
        model = Medic
        fields = [
            'person',
            'role',
            'specialty',
            'company',
        ]

        labels = {
            'person': 'Person',
            'role': 'Role',
            'specialty': 'Specialty',
            'company': 'Company',
        }

        widgets = {
            'person': forms.Select(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'specialty': forms.Select(attrs={'class': 'form-control'}),
            'company': forms.Select(attrs={'class': 'form-control'}),
        }


class PacienteForm(ModelForm):
    class Meta:
        model = Patient
        fields = [
            'person',
            'date_birth',
            'direction',
            'entity',
        ]

        labels = {
            'person': 'Person',
            'date_birth': 'Date birth',
            'direction': 'Direction',
            'entity': 'Entity',
        }

        widgets = {
            'person': forms.Select(attrs={'class': 'form-control'}),
            'date_birth': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'direction': forms.TextInput(attrs={'class': 'form-control'}),
            'entity': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_date_birth(self):
        date_birth = self.cleaned_data.get('date_birth')
        if date_birth > date.today():
            raise forms.ValidationError("The birth date of birth cannot be greater than the current date")
        return date_birth


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = [
            'nit',
            'name',
            'email',
            'phone'
        ]

        labels = {
            'nit': 'Nit',
            'name': 'Name',
            'email': 'Email',
            'phone': 'Phone'
        }

        widgets = {
            'nit': forms.NumberInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'})
        }


class EntityForm(ModelForm):
    class Meta:
        model = Entity

        fields = [
            'name'
        ]

        labels = {
            'name': 'Name'
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }


class SpecialtyForm(ModelForm):
    class Meta:
        model = Specialty

        fields = [
            'name',
            'company'
        ]

        labels = {
            'name': 'Name',
            'company': 'Company'
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.Select(attrs={'class': 'form-control'})
        }


class RoleForm(ModelForm):
    class Meta:
        model = Role

        fields = [
            'name',
            'company'
        ]

        labels = {
            'name': 'Name',
            'company': 'Company'
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.Select(attrs={'class': 'form-control'})
        }


class StudyForm(ModelForm):
    class Meta:
        model = Study
        fields = [
            'name',
            'company'
        ]

        labels = {
            'name': 'Name',
            'company': 'Company'
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.Select(attrs={'class': 'form-control'})
        }


class ExamForm(ModelForm):
    class Meta:
        model = Exam

        fields = [
            'patient',
            'medic',
            'study',
            'status',
            'file',
            'result'
        ]

        labels = {
            'patient': 'Patient',
            'medic': 'Medic',
            'study': 'Study',
            'status': 'Status',
            'file': 'File',
            'result': 'Result'
        }

        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'medic': forms.Select(attrs={'class': 'form-control'}),
            'study': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(choices=StatusChoices.CHOICES, attrs={'class': 'form-control'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
            'result': forms.Textarea(attrs={'class': 'form-control'})
        }
