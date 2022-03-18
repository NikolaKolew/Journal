from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from Journal.auth_accounts.models import AppUser, Profile
from Journal.web_app.views import HomeView

UserModel = get_user_model()

class TestProfileLoginView(TestCase):
    VALID_USER_DATA = {
        'email': 'kolev777@gmail.com',
        'password': 'NikolaKU99881',
    }


