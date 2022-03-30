from django.test import TestCase

from Journal.web_app.forms import CreateJournalForm, EditJournalForm, CreateContactForm


class TestJournalForms(TestCase):
    VALID_JOURNAL_DATA = {
        'title': 'Todays journal...',
        'description': 'This is description',
    }

    INVALID_JOURNAL_DATA = {
        'title': 'T',
        'description': 'This is description',
    }

    VALID_CONTACT_FORM_DATA = {
        'email': 'test@test.com',
        'subject': 'hello',
        'message': 'I found a bug ',
    }
    INVALID_CONTACT_FORM_DATA = {
        'email': 'test@test.com',
        'subject': '',
        'message': 'I found a bug ',
    }

    def test_contact_form_excepts_to_be_valid(self):
        contact = self.VALID_CONTACT_FORM_DATA
        form = CreateContactForm(contact)
        self.assertTrue(form.is_valid())

    def test_contact_form_excepts_to_be_invalid(self):
        contact = self.INVALID_CONTACT_FORM_DATA
        form = CreateContactForm(contact)
        self.assertFalse(form.is_valid())

    def test_create_journal_form_excepts_to_be_valid(self):
        journal = self.VALID_JOURNAL_DATA
        form = CreateJournalForm(journal)
        self.assertTrue(form.is_valid())

    def test_create_journal_form_if_length_less_or_equal_to_one_excepts_validation_error(self):
        journal = self.INVALID_JOURNAL_DATA
        form = CreateJournalForm(journal)
        self.assertFalse(form.is_valid())

    def test_edit_journal_form_excepts_to_be_valid(self):
        edit_journal = self.VALID_JOURNAL_DATA
        form = EditJournalForm(edit_journal)
        self.assertTrue(form.is_valid())

    def test_edit_journal_form_if_length_less_or_equal_to_one_excepts_validation_error(self):
        journal = self.INVALID_JOURNAL_DATA
        form = EditJournalForm(journal)
        self.assertFalse(form.is_valid())