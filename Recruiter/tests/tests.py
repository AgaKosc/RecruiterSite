from django.core.urlresolvers import reverse
from django.urls import resolve
from django.test import TestCase
from Recruiter.views.views import *

class HomeTests(TestCase):
    def test_home_view_status_code(self):
        url = reverse('Recruiter:home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 302)


    def test_home_url_resolves_home_view(self):
        view = resolve('/')  # why failing?
        self.assertEquals(view.func, home)
