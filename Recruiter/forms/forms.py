from django import forms
from multipleselectionfield import MultipleSelectionFormField

from Recruiter.models.models import Question, CategoryType


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
    categoryChoices = [[cat.id, cat.category_name] for cat in CategoryType.objects.all()]
    choices = forms.MultipleChoiceField(label='Category', choices=categoryChoices, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Question
        fields = ['summary', 'content', 'answer']

    def clean(self):
        cleaned_data = super(AddQuestionForm, self).clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        answer = cleaned_data.get('answer')
        if not title and not content and not answer:
            raise forms.ValidationError('You have to write something!')
