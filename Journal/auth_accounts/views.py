from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, get_object_or_404

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from Journal.auth_accounts.forms import UserRegistrationForm, EditProfileForm
from Journal.auth_accounts.models import Profile
from Journal.web_posts.models import Post

UserModel = get_user_model()


class RegisterPage(CreateView):
    form_class = UserRegistrationForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('journals')
    redirect_authenticated_user = True

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('journals')
        return super(RegisterPage, self).get(*args, **kwargs)


class CustomLoginView(LoginView):
    template_name = 'user/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('journals')


class ProfileDetail(LoginRequiredMixin, ListView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'user/profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileDetail, self).get_context_data()
        total_posts = Post.objects.filter(user=self.request.user).count()
        context['total_posts'] = total_posts
        return context


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'user/profile_edit.html'
    form_class = EditProfileForm
    success_url = reverse_lazy('profile-page')
