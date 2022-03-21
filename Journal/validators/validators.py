from django.core.exceptions import ValidationError


def name_only_letters_validator(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('Value must be only letters')


def min_length_validator(value):
    if len(value) <= 1:
        raise ValidationError("Value can't be less or equal to 1")
