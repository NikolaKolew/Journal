from django.test import TestCase

from Journal.auth_accounts.forms import UserRegistrationForm, EditProfileForm


class ProfileFormsTests(TestCase):
    VALID_USER_DATA = {
        'first_name': 'Nikola',
        'last_name': 'Kolev',
        'email': 'kolev777@gmail.com',
        'password1': 'NikolaKU99881',
        'password2': 'NikolaKU99881',
    }

    IVALID_USER_DATA_COINTAINS_DIGITS_IN_NAMES = {
        'first_name': '11Nikola',
        'last_name': 'Kolev22',
        'email': 'kolev777@gmail.com',
        'password1': 'NikolaKU99881',
        'password2': 'NikolaKU99881',
    }


    def test_profile_register_form_valid_data_except_to_be_valid(self):
        data = self.VALID_USER_DATA

        form = UserRegistrationForm(data)
        self.assertTrue(form.is_valid())

    def test_profile_register_form_invalid_data_except_to_be_invalid(self):
        data = self.IVALID_USER_DATA_COINTAINS_DIGITS_IN_NAMES
        form = UserRegistrationForm(data)

        self.assertFalse(form.is_valid())

    def test_profile_edit_form_when_form_is_valid_except_to_be_valid(self):
        data = {
            'first_name': self.VALID_USER_DATA['first_name'],
            'last_name': self.VALID_USER_DATA['last_name'],
        }

        form = EditProfileForm(data)

        self.assertTrue(form.is_valid())

    def test_profile_edit_form_when_form_is_not_valid_except_to_be__not_valid(self):
        data = {
            'first_name': self.IVALID_USER_DATA_COINTAINS_DIGITS_IN_NAMES['first_name'],
            'last_name': self.VALID_USER_DATA['last_name'],
        }

        form = EditProfileForm(data)

        self.assertFalse(form.is_valid())