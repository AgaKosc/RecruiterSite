from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin

from ..models.models import Question
from ..forms.forms import QuestionForm

class AddQuestionView(SuccessMessageMixin, CreateView):
    model = Question
    form_class = QuestionForm
    success_url = reverse_lazy('questions')
    template_name = 'Recruiter/questions/addQuestion.html'
    success_message = "New question was added successfully"

class EditQuestionView(LoginRequiredMixin, UpdateView):
    model = Question
    fields = ('summary', 'content', 'answer', 'category_type')
    template_name = 'Recruiter/questions/editQuestion.html'
    pk_url_kwarg = 'questionId'
    context_object_name = 'question'

    def form_valid(self, form):
        question = form.save(commit=False)
        question.last_change_date = timezone.datetime.now()
        question.save()
        return redirect('questions')