from django.contrib import admin

# Register your models here.
from Journal.web_posts.models import Comment, Post


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ('post', 'user')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ('title', 'user')
