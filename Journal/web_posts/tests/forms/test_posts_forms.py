from django.test import TestCase
from Journal.web_posts.forms import CreatePostForm, EditPostForm, CreateCommentForm, EditCommentForm


class TestsPostForms(TestCase):
    VALID_POST_DATA = {
        'title': 'Hello there',
        'body': 'How are you today',
    }

    INVALID_POST_DATA = {
        'title': 'H',
        'body': 'How are you today',
    }

    VALID_COMMENT_DATA = {
        'description': 'Food post',
    }

    def test_create_post_form_excepts_to_be_valid(self):
        post = self.VALID_POST_DATA
        form = CreatePostForm(post)
        self.assertTrue(form.is_valid())

    def test_edit_post_form_excepts_to_be_valid(self):
        edit_post = self.VALID_POST_DATA
        form = EditPostForm(edit_post)
        self.assertTrue(form.is_valid())

    def test_create_comment_form_excepts_to_be_valid(self):
        comment = self.VALID_COMMENT_DATA
        form = CreateCommentForm(comment)
        self.assertTrue(form.is_valid())

    def test_edit_comment_form_excepts_to_be_valid(self):
        edit_comment = self.VALID_COMMENT_DATA
        form = EditCommentForm(edit_comment)
        self.assertTrue(form.is_valid())

    def test_create_post_form_title_less_or_equal_to_one_excepts_validation_error(self):
        post = self.INVALID_POST_DATA
        form = EditPostForm(post)
        self.assertFalse(form.is_valid())
