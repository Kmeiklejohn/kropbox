from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from kropbox.manager.models import FileObject, Folder
from kropbox.manager.forms import Add_File, Add_Folder
from django.views import View
from kropbox.profile.models import KropboxUser

class FolderView(View):
    folder_form = Add_Folder
    initial = {'key': 'value'}
    html = 'genericForm.html'


    def get(self, request, *args, **kwargs):
        form = self.folder_form(initial=self.initial)
        return render(request, self.html, {'form':form})

    def post(self, request, *args, **kwargs):
        form = self.folder_form(request.POST)
        owner = KropboxUser.objects.filter(user=request.user)
        if form.is_valid():
            data = form.cleaned_data
            folder = Folder.objects.create(
                parent = data['parent'],
                name = data['name'],
                owner = data['owner'])
        else:
            form = Add_Folder
            if not request.user.is_staff:  
                form.fields['owner'].queryset= KropboxUser.objects.filter(user=request.user)
        return render(request, self.html, {'form':form})


class FileView(View):
    file_form = Add_File
    initial = {'key': 'value'}
    html = 'upload.html'


    def get(self, request, *args, **kwargs):
        form = self.file_form(initial=self.initial)
        return render(request, self.html, {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = self.file_form(request.POST)
        owner = KropboxUser.objects.filter(user=request.user)
        if form.is_valid():
            data = form.cleaned_data
            file_object = file_object.objects.create(
                folder = data['parent'],
                name = data['name'],
                owner = data['owner'])
        else:
            form = Add_File
        return render(request, self.html, {'form':form})
