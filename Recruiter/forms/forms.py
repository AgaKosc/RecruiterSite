from django import forms

from Recruiter.models.models import Question


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password (Again)', widget=forms.PasswordInput())


class AddQuestionForm(forms.ModelForm):
    summary = forms.CharField(label='Summary', max_length=100)
    content = forms.CharField(
        max_length=20000,
        widget=forms.Textarea(attrs={'rows':5}),
    )
    answer = forms.CharField(
        max_length=20000,
        widget=forms.Textarea(attrs={'rows':5}),
    )

    class Meta:
        model = Question
        fields = ['summary', 'content', 'answer', 'category_type']
