from django import forms

from Journal.helpers.helpers import BootstrapFormMixin
from Journal.web_posts.models import Post, Comment


class CreatePostForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Post
        fields = ('feeling', 'title', 'body')


class EditPostForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ('user',)


class CreateCommentForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ('user', 'post',)


class EditCommentForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ('user', 'post',)
