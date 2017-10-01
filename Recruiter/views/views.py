from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from Recruiter.models.models import *
from Recruiter.forms.forms import *

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('Recruiter:home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

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
    if request.method == 'POST':
        form = AddQuestionForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = AddQuestionForm()
    return render(request, 'Recruiter/questions/addQuestion.html', {'form': form})