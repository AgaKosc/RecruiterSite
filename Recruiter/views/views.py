import logging

from django.shortcuts import render, get_object_or_404, redirect
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
    if request.method == 'POST':
        form = AddQuestionForm(request.POST)
        if form.is_valid():
            newQuestion = form.save(commit=False)
            Question.objects.create(
                summary=form.cleaned_data.get('summary'),
                content=form.cleaned_data.get('content'),
                answer=form.cleaned_data.get('answer'),
                author=request.user,
                category_type=form.cleaned_data.get('category_type')
            )
            return redirect('questions')
    else:
        form = AddQuestionForm()
    return render(request, 'Recruiter/questions/addQuestion.html', {'form': form})

@login_required()
def editQuestion(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    if request.method == 'POST':
        form = AddQuestionForm(initial={'summary': question.summary,
                                        'content': question.content,
                                        'answer': question.answer,
                                        'category_type': question.category_type})
        if form.is_valid():
            updatedQuestion = form.save(commit=False)
            question.summary=form.cleaned_data.get('summary')
            question.content=form.cleaned_data.get('content')
            question.answer=form.cleaned_data.get('answer')
            question.category_type=form.cleaned_data.get('category_type')
            question.save()
    else:
        form = AddQuestionForm()
    return render(request, 'Recruiter/questions/editQuestion.html', {'form': form})