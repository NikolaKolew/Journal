from django.contrib import admin

# Register your models here.
from Journal.web_posts.models import Comment

admin.site.register(Comment)
