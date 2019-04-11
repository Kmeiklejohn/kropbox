from django import forms
from kropbox.profile.models import KropboxUser, User
from django.utils.translation import gettext_lazy as _
class Add_KropboxUser(forms.ModelForm):
    class Meta:
        model = KropboxUser
        fields = ('name',)
        labels = {
            'name': _('user'),
        }
        help_texts = {
            'name': _('Some useful help text.'),
        }
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }

class SignupForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
