from django.contrib import admin

# Register your models here.
from Journal.web_app.models import Journal, Contact


@admin.register(Journal)
class JournalAdmin(admin.ModelAdmin):
    pass

@admin.register(Contact)
class CommentAdmin(admin.ModelAdmin):
    pass