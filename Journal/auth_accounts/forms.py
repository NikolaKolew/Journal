from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

from Journal.auth_accounts.models import Profile, BanUser
from Journal.helpers.helpers import BootstrapFormMixin

UserModel = get_user_model()


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_CHARS,
    )
    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_CHARS,
    )

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            user=user,
        )
        if commit:
            profile.save()

        return user

    class Meta:
        model = UserModel
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name')


class EditProfileForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'picture', 'description')
        exclude=('user',)


class BanUserForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = BanUser
        fields = ('is_banned',)
        exclude= ('user',)
