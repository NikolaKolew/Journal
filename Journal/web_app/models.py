from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Journal(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    picture = models.FileField(
        null=True,
        blank=True,
    )

    title = models.CharField(
        max_length=200
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
