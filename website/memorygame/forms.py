from django import forms

class UserLoginForm(forms.Form):
    user_name = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput())
    def clean(self):
        cleaned = super(UserLoginForm,self).clean()
        user_name = cleaned.get('user_name')
        password = cleaned.get('password')

class QuestionForm(forms.Form):
    question_id = forms.IntegerField(widget=forms.HiddenInput())
    question = forms.CharField(widget=forms.HiddenInput())
    #answer = forms.CharField(initial='')
    correct_answer = forms.CharField(widget=forms.HiddenInput())


class AnswerForm(forms.Form):
    question_id = forms.IntegerField(widget=forms.HiddenInput())
    question = forms.CharField(widget=forms.HiddenInput())
    answer = forms.CharField(initial='')
    correct_answer = forms.CharField(widget=forms.HiddenInput())
