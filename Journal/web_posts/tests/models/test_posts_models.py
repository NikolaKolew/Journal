from django.core.exceptions import ValidationError
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

    INVALID_POST_CREDENTIALS = {
        # title <= 1 raises ValidationError
        'feeling': 'HAPPY',
        'body': 'Hello',
        'title': 'N',
        'user_id': 1,
    }

    INVALID_USER_FOR_POST_CREDENTIALS = {
        'body': 'Hello',
        'title': 'New post',
        'user_id': 2,
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

    def test_valid_post_invalid_user_excepts_validation_error(self):
        user = AppUser(**self.VALID_USER_CREDENTIALS)
        post = Post(**self.INVALID_USER_FOR_POST_CREDENTIALS)

        with self.assertRaises(ValidationError) as context:
            post.full_clean()
            user.full_clean()
            user.save()
            post.save()
        self.assertIsNotNone(context.exception)

    def test_post_title_less_or_equal_to_one_excepts_validation_error(self):
        user = AppUser(**self.VALID_USER_CREDENTIALS)
        post = Post(**self.INVALID_POST_CREDENTIALS)

        with self.assertRaises(ValidationError) as context:
            post.full_clean()
            user.full_clean()
            user.save()
            post.save()
        self.assertIsNotNone(context.exception)