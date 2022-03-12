from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from Journal.web_posts.forms import EditPostForm
from Journal.web_posts.models import Post

UserModel = get_user_model()

class PostList(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts.html'


class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('title',)
    template_name = 'post_create.html'
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreatePost, self).form_valid(form)


class EditPost(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_update.html'
    form_class = EditPostForm
    success_url = reverse_lazy('posts')

class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')


