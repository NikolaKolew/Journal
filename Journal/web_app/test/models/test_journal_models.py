from django.test import TestCase

from Journal.auth_accounts.models import AppUser
from Journal.web_app.models import Journal


class TestJournals(TestCase):
    VALID_USER_CREDENTIALS = {
        'email': 'kolev777@gmail.com',
    }

    VALID_JOURNAL_CREDENTIALS = {
        'title': 'First journal',
        'description': 'Hello there',
        'user_id': 1,
    }

    def test_journal_create_expects_success(self):
        user = AppUser(**self.VALID_USER_CREDENTIALS)
        journal = Journal(**self.VALID_JOURNAL_CREDENTIALS)
        user.save()
        journal.save()

        self.assertIsNotNone(journal.pk)
