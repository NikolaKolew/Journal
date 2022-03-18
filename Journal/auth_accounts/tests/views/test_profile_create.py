from django.test import TestCase
from django.urls import reverse

from Journal.auth_accounts.models import AppUser, Profile


class ProfileCreateView(TestCase):
    VALID_USER_DATA = {
        'first_name': 'Nikola',
        'last_name': 'Kolev',
        'email': 'kolev777@gmail.com',
        'password1': 'NikolaKU99881',
        'password2': 'NikolaKU99881',
    }

    def test_create_profile_valid_data(self):
        self.client.post(
            reverse('register'),
            data=self.VALID_USER_DATA,
        )

        user = AppUser.objects.first()
        profile = Profile.objects.first()

        self.assertIsNotNone(user)
        self.assertIsNotNone(profile)
        self.assertEqual(self.VALID_USER_DATA['first_name'], profile.first_name)
        self.assertEqual(self.VALID_USER_DATA['last_name'], profile.last_name)
        self.assertEqual(self.VALID_USER_DATA['email'], user.email)

    def test_create_profile_valid_data_except_to_redirect_to_home_page(self):
        response = self.client.post(
            reverse('register'),
            data=self.VALID_USER_DATA,
        )

        expected_url = reverse('home')
        self.assertRedirects(response, expected_url)




