from django.contrib import admin

# Register your models here.
from Journal.auth_accounts.models import AppUser, Profile, BanUser


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(BanUser)
class BanUserAdmin(admin.ModelAdmin):
    pass