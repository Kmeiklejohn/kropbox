from django import forms
from kropbox.profile.models import KropboxUser, Submission

class SignupForm(forms.Form):
    username = forms.CharField(label=" Username.", max_length=50)
    email = forms.EmailField(label="Email", )
    password = forms.CharField(widget=forms.PasswordInput())

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
