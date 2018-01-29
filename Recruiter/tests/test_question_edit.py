from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from ..models.models import Question, CategoryType


class QuestionEditViewTestCase(TestCase):

    def setUp(self):
        self.username = 'john'
        self.password = '123'
        user = User.objects.create_user(username=self.username, email='john@doe.com', password=self.password)
        self.categoryType = CategoryType.objects.create(category_name='xxx')
        self.question = Question.objects.create(summary='aaa', content='bbb', answer='ccc', author=user,
                                                category_type=self.categoryType)
        self.url = reverse('editQuestion', kwargs={'questionId': self.question.pk})

class LoginRequiredQuestionEditViewTests(QuestionEditViewTestCase):

    def test_redirectionForNotLoggedUser(self):
        login_url = reverse('login')
        response = self.client.get(self.url)
        self.assertRedirects(response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))

class UnauthorizedQuestionEditViewTests(QuestionEditViewTestCase):
    def setUp(self):
        '''
        Create a new user different from the one who posted
        '''
        super().setUp()
        username = 'jane'
        password = '321'
        user = User.objects.create_user(username=username, email='jane@doe.com', password=password)
        self.client.login(username=username, password=password)
        self.response = self.client.get(self.url)

class QuestionEditViewTests(QuestionEditViewTestCase):
    def setUp(self):
        super().setUp()
        self.client.login(username=self.username, password=self.password)
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_form_inputs(self):
        '''
        The view must contain two inputs: csrf, message textarea
        '''
        self.assertContains(self.response, '<input', 2)
        self.assertContains(self.response, '<textarea', 2)
        self.assertContains(self.response, '<select', 1)