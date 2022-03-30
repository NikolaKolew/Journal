from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from Journal.auth_accounts.models import Profile
from Journal.web_app.models import Journal

UserModel = get_user_model()


class TestJournalViews(TestCase):
    VALID_USER_DATA = {
        'email': 'kolev777@gmail.com',
        'password': 'NikolaKU99881',
    }
    VALID_PROFILE_DATA = {
        'first_name': 'Nikola',
        'last_name': 'Kolev',

    }

    VALID_JOURNAL_DATA = {
        'title': 'Hello',
        'description': 'some description',
    }

    VALID_CONTACT_DATA = {
        'email': 'test@test.com',
        'subject': 'hello',
        'message': 'I found a bug ',
    }

    def __create_journal_for_user(self, user):
        journal = Journal.objects.create(
            **self.VALID_JOURNAL_DATA,
            user=user,
        )

        journal.save()
        return journal

    def __create_user(self, **data):
        user = UserModel.objects.create_user(**data)
        return user

    def __create_profile_and_user(self):
        user = self.__create_user(**self.VALID_USER_DATA)
        profile = Profile.objects.create(**self.VALID_PROFILE_DATA, user=user)
        return user, profile

    def __get_journal_details(self, journal):
        return self.client.get(reverse('details', kwargs={'pk': journal.pk}))

    def __get_all_journals(self):
        return self.client.get(reverse('journals'))

    def test_shows_all_journals_page(self):
        user, profile = self.__create_profile_and_user()
        self.__create_journal_for_user(user)
        self.__get_all_journals()
        self.assertTemplateUsed('journal/journals.html')

    def test_get_journal_detail_page(self):
        user, profile = self.__create_profile_and_user()
        journal = self.__create_journal_for_user(user)
        self.__get_journal_details(journal)
        self.assertTemplateUsed('journal/journal_details.html')

    def test_create_journal_valid_data(self):
        user, profile = self.__create_profile_and_user()
        self.__create_journal_for_user(user)
        self.client.post(
            reverse('create-journal'),
            data=self.VALID_JOURNAL_DATA,
        )

        journal = Journal.objects.first()
        self.assertIsNotNone(journal)
        self.assertEqual(self.VALID_JOURNAL_DATA['title'], journal.title)

    def test_contact_form_valid_data_if_user_is_not_authenticated(self):
        response = self.client.post(
            reverse('contact'),
            data=self.VALID_CONTACT_DATA,
        )
        expected_url = reverse('index')
        self.assertRedirects(response, expected_url)
