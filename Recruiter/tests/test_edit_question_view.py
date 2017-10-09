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
                                                category_name=self.categoryType)
        self.url = reverse('editQuestion', kwargs={
            'questionId': self.question.pk
        })

class LoginRequiredQuestionEditViewTests(QuestionEditViewTestCase):
    def test_redirectionForNotLoggedUser(self):
        login_url = reverse('login')
        response = self.client.get(self.url)
        self.assertRedirects(response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))
