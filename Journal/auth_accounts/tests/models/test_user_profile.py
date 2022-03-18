from django.core.exceptions import ValidationError
from django.test import TestCase

from Journal.auth_accounts.models import Profile, AppUser


class ProfileTests(TestCase):
    VALID_PROFILE_CREDENTIALS = {
        'first_name': 'Nikola',
        'last_name': 'Kolev',
        'user_id': 1,
    }

    VALID_USER_CREDENTIALS = {
        'email': 'kolev777@gmail.com',
    }

    def test_profile_create_when_first_name_contains_only_letters__success(self):
        user = AppUser(**self.VALID_USER_CREDENTIALS)
        profile = Profile(**self.VALID_PROFILE_CREDENTIALS)
        user.save()
        profile.save()
        self.assertIsNotNone(profile.pk)

    def test_first_name_contains_digit__expects_to_fail(self):
        first_name = '1Nikola11'
        profile = Profile(
            first_name=first_name,
            last_name=self.VALID_PROFILE_CREDENTIALS['last_name'],
            user_id=self.VALID_PROFILE_CREDENTIALS['user_id']
        )
        user = AppUser(**self.VALID_USER_CREDENTIALS)
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            user.full_clean()
            user.save()
            profile.save()
        self.assertIsNotNone(context.exception)

    def test_last_name_contains_digit__expects_to_fail(self):
        last_name = '1Nikola11'
        profile = Profile(
            first_name=self.VALID_PROFILE_CREDENTIALS['first_name'],
            last_name=last_name,
            user_id=self.VALID_PROFILE_CREDENTIALS['user_id']
        )
        user = AppUser(**self.VALID_USER_CREDENTIALS)
        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            user.full_clean()
            user.save()
            profile.save()
        self.assertIsNotNone(context.exception)