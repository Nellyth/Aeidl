from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError


def positive_integer_field(value):
    """
    Args:
        value: str to int

    Returns: ValidationError

    """
    try:
        value = int(value)
        if value < 0:
            raise ValidationError(_("This field only allows positive numerical data."), params={'value': value})
    except ValueError:
        raise ValidationError(_("This field only allows positive numerical data."), params={'value': value})
