from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, TemplateView

from Journal.web_app.forms import EditJournalForm, CreateJournalForm
from Journal.web_app.models import Journal

UserModel = get_user_model()


# if request.path

# TODO make CBV for the index page
# def index_view(request):
#     return render(request, 'index.html')

class IndexView(TemplateView):
    template_name = 'index.html'


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'


class ProfileList(LoginRequiredMixin, ListView):
    model = Journal
    context_object_name = 'journals'
    template_name = 'journal/journals.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['journals'] = context['journals'].filter(user=self.request.user)
        return context


class CreateJornal(LoginRequiredMixin, CreateView):
    model = Journal
    form_class = CreateJournalForm
    success_url = reverse_lazy('journals')
    template_name = 'journal/journal_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateJornal, self).form_valid(form)


class JournalDetail(LoginRequiredMixin, DetailView):
    model = Journal
    context_object_name = 'journal'
    template_name = 'journal/journal_details.html'


class JournalUpdate(LoginRequiredMixin, UpdateView):
    model = Journal
    template_name = 'journal/journal_update.html'
    form_class = EditJournalForm
    success_url = reverse_lazy('journals')


class JournalDelete(LoginRequiredMixin, DeleteView):
    model = Journal
    template_name = 'journal/journal_delete.html'
    context_object_name = 'journal'
    success_url = reverse_lazy('journals')
