# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-08 08:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Recruiter', '0002_auto_20171001_1027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questioncategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='questioncategory',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='category_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Recruiter.CategoryType'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='QuestionCategory',
        ),
    ]
