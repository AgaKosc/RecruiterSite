from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from Recruiter.views.views import *


class HomePageTests(TestCase):
    def setUp(self):
        self.url = reverse('home')
        self.response = self.client.get(self.url)
