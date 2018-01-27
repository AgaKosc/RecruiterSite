from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class CategoryType(models.Model):
    category_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.category_name


class Question(models.Model):
    author = models.ForeignKey(User)
    summary = models.CharField(max_length=100, unique=True)
    content = models.TextField(max_length=5000, null=True)
    answer = models.TextField(max_length=5000, null=True)
    category_type = models.ForeignKey(CategoryType)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_change_date = models.DateField(auto_now_add=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.summary


class QuestionVotes(models.Model):
    user = models.ForeignKey('auth.User')
    question = models.ForeignKey(Question)
    vote = models.IntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.user + " " + self.question.summary + " " + self.vote
