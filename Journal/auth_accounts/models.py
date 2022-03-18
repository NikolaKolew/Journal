from annoying.fields import AutoOneToOneField
from django.db import models
from django.contrib.auth import models as auth_models

from Journal.auth_accounts.managers import AppUsersManager
from Journal.validators.validators import name_only_letters_validator


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

    def __str__(self):
        return f'{self.email}'


class Profile(models.Model):
    FIRST_NAME_MAX_CHARS = 25
    LAST_NAME_MAX_CHARS = 25

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_CHARS,
        validators=(
            name_only_letters_validator,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_CHARS,
        validators=(
            name_only_letters_validator,
        )
    )

    followers = models.IntegerField(
        default=0,
    )

    description = models.TextField(
        null=True,
        blank=True,
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

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class BanUser(models.Model):
    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    is_banned = models.BooleanField(
        default=False,
    )

