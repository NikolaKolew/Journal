from django.db import models
from django.contrib.auth import models as auth_models

from Journal.auth_accounts.managers import AppUsersManager


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'

    objects = AppUsersManager()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
    )

    last_name = models.CharField(
        max_length=100,

    )

    picture = models.FileField(
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
