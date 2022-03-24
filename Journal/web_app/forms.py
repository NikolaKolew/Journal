from django import forms

from Journal.helpers.helpers import BootstrapFormMixin
from Journal.web_app.models import Journal, Contact


class EditJournalForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Journal
        fields = '__all__'
        exclude = ('user',)


class CreateJournalForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Journal
        fields = '__all__'
        exclude = ('user',)


class CreateContactForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Contact
        fields = '__all__'
