from django.test import TestCase
from .forms import CollaborateForm


# Create your tests here.
class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Fred',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_form_is_invalid_name(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': '',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(form.is_valid(), msg="No name-form should be invalid")

    def test_form_is_invalid_email(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Joe',
            'email': '',
            'message': 'Bonjour!'
        })
        self.assertFalse(form.is_valid(),
                         msg="No email-form should be invalid")

    def test_form_is_invalid_message(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'Elias',
            'email': 'test@anothertest.com',
            'message': ''
        })
        self.assertFalse(form.is_valid(),
                         msg="No message-form should be invalid")
