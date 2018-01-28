import logging

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from Recruiter.models.models import *
from Recruiter.forms.forms import *
from Recruiter.Helpers.filters import QuestionFilter

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%m-%d %H:%M')

@login_required()
def home(request):
    return render(request, 'Recruiter/home.html')

@login_required()
def questions(request):
    questionList = Question.objects.order_by('summary')
    question_filter = QuestionFilter(request.GET, queryset=questionList)
    context = {'questionList': questionList, 'filter': question_filter}
    return render(request, 'Recruiter/questions/questions.html', context)


@login_required()
def detail(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    return render(request, 'Recruiter/questions/questionDetail.html', {'question': question})


@login_required()
def addQuestion(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            Question.objects.create(
                summary=form.cleaned_data.get('summary'),
                content=form.cleaned_data.get('content'),
                answer=form.cleaned_data.get('answer'),
                author=request.user,
                category_type=form.cleaned_data.get('category_type')
            )
            return redirect('questions')
        else:
            for err in form.errors:
                logging.error(err)
    else:
        form = QuestionForm()
    return render(request, 'Recruiter/questions/addQuestion.html', {'form': form})

@login_required()
def editQuestion(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save(commit=False)
            question.summary=form.cleaned_data.get('summary')
            question.content=form.cleaned_data.get('content')
            question.answer=form.cleaned_data.get('answer')
            question.category_type=form.cleaned_data.get('category_type')
            question.save()
            return redirect('questions')
    else:
        form = QuestionForm(instance=question)
    return render(request, 'Recruiter/questions/editQuestion.html', {'form': form})