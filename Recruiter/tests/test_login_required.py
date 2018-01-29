from django.core.urlresolvers import reverse
from django.test import TestCase


class LoginRequiredTests(TestCase):

    def setUp(self):
        self.url = reverse('home')
        self.response = self.client.get(self.url)

    def test_redirection(self):
        login_url = reverse('login')
        self.assertRedirects(self.response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))
