from django.conf.urls import url
from django.contrib.auth import views as auth_views

from Recruiter.views import views

app_name = 'Recruiter'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^questions/$', views.questions, name='questions'),
    url(r'^(?P<questionId>[0-9]+)/$', views.detail, name='detail'),
    url(r'^addQuestion/$', views.addQuestion, name='addQuestion'),
]