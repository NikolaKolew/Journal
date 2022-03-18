from django.core.exceptions import ValidationError


def name_only_letters_validator(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Value must be only letters')