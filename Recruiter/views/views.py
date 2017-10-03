from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from Recruiter.models.models import *
from Recruiter.forms.forms import *

@login_required()
def home(request):
    return render(request, 'Recruiter/home.html')

@login_required()
def questions(request):
    questionList = Question.objects.order_by('summary')
    context = {'questionList': questionList}
    return render(request, 'Recruiter/questions/questions.html', context)

@login_required()
def detail(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    return render(request, 'Recruiter/questions/questionDetail.html', {'question': question})

@login_required()
def addQuestion(request):
    user = User.objects.first()
    if request.method == 'POST':
        form = AddQuestionForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = AddQuestionForm()
    return render(request, 'Recruiter/questions/addQuestion.html', {'form': form})