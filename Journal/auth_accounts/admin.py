from django.contrib import admin

# Register your models here.
from Journal.auth_accounts.models import AppUser, Profile, BanUser


@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    list_filter = ('is_staff', 'groups')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_filter = ('first_name',)

@admin.register(BanUser)
class BanUserAdmin(admin.ModelAdmin):
    list_filter = ('is_banned',)
