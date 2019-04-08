from django import forms
from mptt.forms import TreeNodeChoiceField
from kropbox.manager.models import Folder, FileObject
from kropbox.profile.models import KropboxUser

class Add_Folder(forms.Form):
    parent = TreeNodeChoiceField(queryset=Folder.objects.all())
    name = forms.CharField(max_length=60)
    owner = forms.ModelChoiceField(queryset=KropboxUser.objects.all())

class Add_File(forms.Form):
    parent = TreeNodeChoiceField(queryset=Folder.objects.all())
    document = forms.FileField(label='select a file')
    name = forms.CharField(max_length=60)
