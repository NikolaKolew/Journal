from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import redirect, get_object_or_404

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView

from Journal.auth_accounts.forms import UserRegistrationForm, EditProfileForm, BanUserForm
from Journal.auth_accounts.models import Profile, BanUser
from Journal.web_posts.models import Post

UserModel = get_user_model()


class RegisterPage(CreateView):
    form_class = UserRegistrationForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('home')
    redirect_authenticated_user = True

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegisterPage, self).get(*args, **kwargs)


class CustomLoginView(LoginView):
    template_name = 'user/login.html'
    # fields = '__all__'
    # redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class ProfileDetail(LoginRequiredMixin, DetailView):
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

    # success_url = reverse_lazy('profile-page')
    def get_success_url(self):
        profile_id = Profile.objects.filter(user_id=self.kwargs['pk']).get().user_id
        return reverse_lazy('profile-page', kwargs={'pk': profile_id})


class BanUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BanUser
    template_name = 'user/ban_user.html'
    form_class = BanUserForm
    success_url = reverse_lazy('dashboard')

    def test_func(self):
        return self.request.user.email.endswith('@staff.com')

    def get_context_data(self, **kwargs):
        context = super(BanUpdate, self).get_context_data()
        user = get_object_or_404(UserModel, id=self.kwargs['pk'])
        context['user'] = user
        return context


class DashboardStaff(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Profile
    template_name = 'user/staff_dashboard.html'

    def test_func(self):
        return self.request.user.email.endswith('@staff.com' or '@admin.com')

    def get_context_data(self, **kwargs):
        context = super(DashboardStaff, self).get_context_data()
        total_posts = Post.objects.filter().count()
        total_users = get_user_model().objects.all()
        context['total_posts'] = total_posts
        context['total_users'] = total_users
        return context


class UserChangePassword(LoginRequiredMixin, PasswordChangeView):
    template_name = 'user/change_password.html'
    success_url = reverse_lazy('login')
