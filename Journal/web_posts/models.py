from django.contrib.auth import get_user_model
from django.db import models

from Journal.validators.validators import min_length_validator

UserModel = get_user_model()


class Post(models.Model):
    HAPPY = 'happy'
    EXCITED = 'excited'
    MOTIVATED = 'motivated'
    THANKFUL = 'thankful'
    GRATEFUL = 'grateful'

    FEELS = [(x, x) for x in (HAPPY, EXCITED, MOTIVATED, THANKFUL, GRATEFUL)]

    TITLE_MAX_CHARS = 50

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    feeling = models.CharField(
        max_length=max(len(x) for (x, _) in FEELS),
        choices=FEELS,
        blank=True,
        null=True,
    )

    body = models.TextField(
        null=True,
        blank=True,
    )

    title = models.CharField(
        max_length=TITLE_MAX_CHARS,
        validators=(
            min_length_validator,
        )
    )

    like = models.ManyToManyField(
        UserModel,
        related_name='post_likes',
    )

    create = models.DateTimeField(
        auto_now_add=True,
    )

    def total_likes(self):
        return self.like.count()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['create']


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    description = models.TextField()

    create = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ['create']

    def __str__(self):
        return f'Post ID: {self.post_id} | Post title: {self.post.title}'