from django.contrib import admin
from Recruiter.models.models import *

# Register your models here.
admin.site.register(Question)
admin.site.register(QuestionVotes)
admin.site.register(CategoryType)