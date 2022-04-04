from django.contrib.auth import get_user_model
from django.db import models

from Journal.validators.validators import min_length_validator

from cloudinary.models import CloudinaryField


UserModel = get_user_model()


class Journal(models.Model):
    TITLE_MAX_CHARS = 50
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    picture = CloudinaryField('image')

    title = models.CharField(
        max_length=TITLE_MAX_CHARS,
        validators=(
            min_length_validator,
        )
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    create = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['create']


class Contact(models.Model):
    SUBJECT_MAX_LENGTH = 20

    email = models.EmailField()
    subject = models.CharField(
        max_length=SUBJECT_MAX_LENGTH,
        validators=(
            min_length_validator,
        )
    )
    message = models.TextField()

    def __str__(self):
        return f'{self.email}'
