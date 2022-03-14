from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from Journal.web_posts.forms import EditPostForm, CreateCommentForm, EditCommentForm
from Journal.web_posts.models import Post, Comment

UserModel = get_user_model()


class PostList(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts.html'


class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post_details.html'


class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('title',)
    template_name = 'post_create.html'
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreatePost, self).form_valid(form)


class CreateComment(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CreateCommentForm
    context_object_name = 'comment'
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super(CreateComment, self).form_valid(form)

    def get_success_url(self):
        post_id = self.kwargs['pk']
        return reverse_lazy('detail-post', kwargs={'pk': post_id})


class EditPost(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_update.html'
    form_class = EditPostForm
    success_url = reverse_lazy('posts')


class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')


class EditComment(LoginRequiredMixin, UpdateView):
    model = Comment
    template_name = 'update_comment.html'
    form_class = EditCommentForm
    success_url = reverse_lazy('posts')


class DeleteComment(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'delete_comment.html'
    success_url = reverse_lazy('posts')
