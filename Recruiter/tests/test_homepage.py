from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from Recruiter.views.views import *


class HomePageTests(TestCase):
    def setUp(self):
        self.url = reverse('Recruiter:home')
        self.response = self.client.get(self.url)

    def test_redirection(self):
        view = resolve('login')  # why failing?
        self.assertRedirects(self.response, 'login?next={url}'.format(url=self.url))
