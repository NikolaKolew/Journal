from django.db.models.signals import post_save
from django.dispatch import receiver

from Journal.auth_accounts.models import AppUser, BanUser


@receiver(post_save, sender=AppUser)
def create_model_ban(sender, instance, created, **kwargs):
    if created:
        BanUser.objects.create(user=instance)