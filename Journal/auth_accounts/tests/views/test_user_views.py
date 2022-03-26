from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from Journal.auth_accounts.models import Profile

UserModel = get_user_model()


class TestProfileDetails(TestCase):
    VALID_USER_DATA = {
        'email': 'kolev777@gmail.com',
        'password': 'NikolaKU99881',
    }
    VALID_PROFILE_DATA = {
        'first_name': 'Nikola',
        'last_name': 'Kolev',

    }

    def __create_user(self, **data):
        user = UserModel.objects.create_user(**data)

        return user

    def __create_profile_and_user(self):
        user = self.__create_user(**self.VALID_USER_DATA)
        profile = Profile.objects.create(**self.VALID_PROFILE_DATA, user=user)

        return (user, profile)

    def __get_profile_details(self, profile):
        return self.client.get(reverse('profile-page', kwargs={'pk': profile.pk}))

    def test_shows_correct_profile_detail_page(self):
        _, profile = self.__create_profile_and_user()
        self.__get_profile_details(profile)
        self.assertTemplateUsed('user/profile.html')


