from django.test import TestCase

from Journal.auth_accounts.models import AppUser
from Journal.web_posts.models import Post, Comment


class TestPostsModels(TestCase):
    VALID_USER_CREDENTIALS = {
        'email': 'kolev777@gmail.com',
    }

    VALID_POST_CREDENTIALS = {
        'feeling': 'HAPPY',
        'body': 'Hello',
        'title': 'New post',
        'user_id': 1,
    }

    VALID_COMMENT_CREDENTIALS = {
        'post_id': 1,
        'user_id': 1,
        'description': 'Hello there',
    }

    def test_valid_post_excepts_success(self):
        user = AppUser(**self.VALID_USER_CREDENTIALS)
        post = Post(**self.VALID_POST_CREDENTIALS)
        user.save()
        post.save()
        self.assertIsNotNone(post.pk)

    def test_valid_comment_with_valid_post_excepts_success(self):
        user = AppUser(**self.VALID_USER_CREDENTIALS)
        post = Post(**self.VALID_POST_CREDENTIALS)
        comment = Comment(**self.VALID_COMMENT_CREDENTIALS)
        user.save()
        post.save()
        comment.save()
        self.assertIsNotNone(comment.pk)