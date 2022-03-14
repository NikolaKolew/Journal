from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from Journal.web_posts.forms import EditPostForm, CreateCommentForm, EditCommentForm, CreatePostForm
from Journal.web_posts.models import Post, Comment

UserModel = get_user_model()


class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'posts/post_create.html'
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreatePost, self).form_valid(form)


class PostList(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/posts.html'
    ordering = ['-create']


class PostDetail(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'posts/post_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetail, self).get_context_data()
        likes = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = likes.total_likes()
        context['total_likes'] = total_likes
        return context


class CreateComment(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CreateCommentForm
    context_object_name = 'comment'
    template_name = 'posts/add_comment.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.post_id = self.kwargs['pk']
        return super(CreateComment, self).form_valid(form)

    def get_success_url(self):
        post_id = self.kwargs['pk']
        return reverse_lazy('detail-post', kwargs={'pk': post_id})


class EditPost(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'posts/post_update.html'
    form_class = EditPostForm
    success_url = reverse_lazy('posts')


class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('posts')


class EditComment(LoginRequiredMixin, UpdateView):
    model = Comment
    template_name = 'posts/update_comment.html'
    form_class = EditCommentForm
    success_url = reverse_lazy('posts')


class DeleteComment(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'posts/delete_comment.html'
    success_url = reverse_lazy('posts')


def like_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    post.like.add(request.user)
    return HttpResponseRedirect(reverse('detail-post', args=[str(pk)]))
