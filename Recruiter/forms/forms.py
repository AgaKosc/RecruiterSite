from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password (Again)', widget=forms.PasswordInput())


class AddQuestionForm(forms.Form):
    summary = forms.CharField(label='Summary', max_length=100)
    content = forms.CharField(
        max_length=20000,
        widget=forms.Textarea(),
    )
    answer = forms.CharField(
        max_length=20000,
        widget=forms.Textarea(),
    )

    def clean(self):
        cleaned_data = super(AddQuestionForm, self).clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        answer = cleaned_data.get('answer')
        if not title and not content and not answer:
            raise forms.ValidationError('You have to write something!')
