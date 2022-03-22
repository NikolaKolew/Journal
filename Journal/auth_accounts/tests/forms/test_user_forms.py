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

    INVALID_USER_DATA_CONTAINS_DIGITS_IN_NAMES = {
        'first_name': '11Nikola',
        'last_name': 'Kolev22',
        'email': 'kolev777@gmail.com',
        'password1': 'NikolaKU99881',
        'password2': 'NikolaKU99881',
    }

    def test_profile_register_form_valid_data_expects_to_be_valid(self):
        data = self.VALID_USER_DATA

        form = UserRegistrationForm(data)
        self.assertTrue(form.is_valid())

    def test_profile_register_form_invalid_data_expects_to_be_invalid(self):
        data = self.INVALID_USER_DATA_CONTAINS_DIGITS_IN_NAMES
        form = UserRegistrationForm(data)

        self.assertFalse(form.is_valid())

    def test_profile_edit_form_when_form_is_valid_expects_to_be_valid(self):
        data = {
            'first_name': self.VALID_USER_DATA['first_name'],
            'last_name': self.VALID_USER_DATA['last_name'],
        }

        form = EditProfileForm(data)

        self.assertTrue(form.is_valid())

    def test_profile_edit_form_when_name_is_less_or_equal_to_one_expects_validation_error(self):
        data = {
            'first_name': 'N',
            'last_name': self.VALID_USER_DATA['last_name'],
        }

        form = EditProfileForm(data)

        self.assertFalse(form.is_valid())

    def test_profile_edit_form_when_form_is_not_valid_expects_to_be__not_valid(self):
        data = {
            'first_name': self.INVALID_USER_DATA_CONTAINS_DIGITS_IN_NAMES['first_name'],
            'last_name': self.VALID_USER_DATA['last_name'],
        }

        form = EditProfileForm(data)

        self.assertFalse(form.is_valid())
