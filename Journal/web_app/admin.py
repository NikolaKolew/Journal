from django.contrib import admin

# Register your models here.
from Journal.web_app.models import Journal, Contact


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    list_filter = ('title',)

@admin.register(Contact)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ('message',)