"""RecruiterSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import logging

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from Recruiter.views.QuestionView import AddQuestionView, EditQuestionView
from Recruiter.views import views
from accounts import views as account_views


logging.basicConfig(filename="logs.txt")

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^signup/$', account_views.signup, name='signup'),
    url(r'^questions/$', views.questions, name='questions'),
    url(r'^questions/(?P<questionId>[0-9]+)/$', views.detail, name='detail'),
    url(r'^questions/add/$', login_required(AddQuestionView.as_view()), name='addQuestion'),
    url(r'^questions/edit/(?P<questionId>[0-9]+)/$', login_required(EditQuestionView.as_view()), name='editQuestion'),
    url(r'^admin/', admin.site.urls),
]
