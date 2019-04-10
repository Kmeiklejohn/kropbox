from django import forms
from kropbox.profile.models import KropboxUser, User

class Add_KropboxUser(forms.Form):

    name = forms.CharField(max_length=50)
    user = forms.ModelChoiceField(
        queryset=User.objects.all())

class SignupForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
