from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class Post(models.Model):
    # TODO add choices for how the user feels

    TITLE_MAX_CHARS = 100

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    title = models.CharField(
        max_length=TITLE_MAX_CHARS,
    )

    create = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['create']

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE)
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
    description = models.TextField()
    create = models.DateTimeField(
        auto_now_add=True,
    )


