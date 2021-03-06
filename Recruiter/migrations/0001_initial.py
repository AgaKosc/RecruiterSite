# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 15:36
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=200)),
                ('content', models.TextField(max_length=1000, null=True)),
                ('answer', models.TextField(max_length=1000, null=True)),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_change_date', models.DateField(default=django.utils.timezone.now)),
                ('votes', models.IntegerField(default=0)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuestionCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recruiter.CategoryType')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recruiter.Question')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionVotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recruiter.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
