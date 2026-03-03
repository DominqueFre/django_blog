from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase

from blog.forms import CommentForm
from .forms import CollaborateForm
from .models import Collaborate, Abouts


class TestAboutCollaborateViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.about = Abouts.objects.create(
            developer="Test Developer",
            author=self.user,
            content="Test content",
        )
        self.collaborate = Collaborate.objects.create(
            name="Test Collaborator",
            email="test@example.com",
            message="Test message"
        )

    def test_render_about_detail_page_with_collaborate_form(self):
        response = self.client.get(reverse(
            'about_info'))
        print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test Developer", response.content)
        self.assertIn(b"Test content", response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)
from django.test import TestCase

# Create your tests here.
