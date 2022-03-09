from django.contrib.auth import login, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from Journal.web_app.models import Journal, Profile

UserModel = get_user_model()


def index_view(request):
    return render(request, 'index.html')

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=25)

    class Meta:
        model = UserModel
        fields = ('email',)

    def clean_first_name(self):
        return self.cleaned_data['first_name']

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            user=user,
        )
        if commit:
            profile.save()

        return user

class RegisterPage(CreateView):
    form_class = UserRegistrationForm
    template_name = 'register.html'
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
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('journals')

# class RegisterPage(FormView):
#     template_name = 'register.html'
#     form_class = UserCreationForm
#     redirect_authenticated_user = True
#     success_url = reverse_lazy('journals')
#
#     def form_valid(self, form):
#         user = form.save()
#         if user is not None:
#             login(self.request, user)
#         return super(RegisterPage, self).form_valid(form)
#
#     def get(self, *args, **kwargs):
#         if self.request.user.is_authenticated:
#             return redirect('journals')
#         return super(RegisterPage, self).get(*args, **kwargs)




class ProfileList(LoginRequiredMixin, ListView):
    model = Journal
    context_object_name = 'journals'
    template_name = 'journals.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['journals'] = context['journals'].filter(user=self.request.user)
        return context


class CreateJornal(LoginRequiredMixin, CreateView):
    model = Journal
    fields = ('title', 'description')
    success_url = reverse_lazy('journals')
    template_name = 'journal_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateJornal, self).form_valid(form)


class JournalDetail(LoginRequiredMixin, DetailView):
    model = Journal
    context_object_name = 'journal'
    template_name = 'journal_details.html'

class ProfileDetail(LoginRequiredMixin, ListView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'profile.html'


class JournalUpdate(LoginRequiredMixin, UpdateView):
    model = Journal
    template_name = 'journal_update.html'
    fields = ('title', 'description')
    success_url = reverse_lazy('journals')


class JournalDelete(LoginRequiredMixin, DeleteView):
    model = Journal
    template_name = 'journal_delete.html'
    context_object_name = 'journal'
    success_url = reverse_lazy('journals')
