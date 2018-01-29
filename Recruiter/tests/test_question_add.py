from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse

from ..views.views import addQuestion
from ..models.models import CategoryType, Question


class NewQuestionTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='john', email='john@doe.com', password='123')
        self.client.login(username='john', password='123')

    def test_add_question_view_success_status_code(self):
        url = reverse('addQuestion')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_new_question_url_resolves_new_question_view(self):
        view = resolve('/questions/add/')
        self.assertEquals(view.func, addQuestion)

    def test_csrf(self):
        url = reverse('addQuestion')
        response = self.client.get(url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    """
    def test_new_topic_valid_post_data(self):
        url = reverse('addQuestion')
        categoryType = CategoryType.objects.create(category_name='xxx')
        data = {"summary":'aaa', 'content':'bbb', 'answer':'ccc', 'category_type':categoryType}
        self.client.post(url, data)
        self.assertTrue(Question.objects.exists())
        """

    """
    def test_new_topic_invalid_post_data(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('new_topic', kwargs={'pk': 1})
        response = self.client.post(url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)

    def test_new_topic_invalid_post_data_empty_fields(self):
        '''
        Invalid post data should not redirect
        The expected behavior is to show the form again with validation errors
        '''
        url = reverse('new_topic', kwargs={'pk': 1})
        data = {
            'subject': '',
            'message': ''
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, 200)
        self.assertFalse(Topic.objects.exists())
        self.assertFalse(Post.objects.exists())


class LoginRequiredNewTopicTests(TestCase):
    def setUp(self):
        Board.objects.create(name='Django', description='Django board.')
        self.url = reverse('new_topic', kwargs={'pk': 1})
        self.response = self.client.get(self.url)

    def test_redirection(self):
        login_url = reverse('login')
        self.assertRedirects(self.response, '{login_url}?next={url}'.format(login_url=login_url, url=self.url))
    """