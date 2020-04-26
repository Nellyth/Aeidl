from django import template

from AppAeidl.models import Medic, Patient

register = template.Library()


@register.filter
def medic_query(value):
    try:
        return Medic.objects.get(person=value).pk
    except Medic.DoesNotExist:
        return None


@register.filter
def patient_query(value):
    try:
        return Patient.objects.get(person=value).pk
    except Patient.DoesNotExist:
        return None
