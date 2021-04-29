from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from polls.models import Author,  Book
import datetime

# Create your tests here.

class AuthorListViewTest(TestCase):
    
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/polls/authors/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'polls/author_list.html')
