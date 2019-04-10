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
        form = self.folder_form(request, initial=self.initial)
        return render(request, self.html, {'form':form})

    def post(self, request, *args, **kwargs):
        form = self.folder_form(request, request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            folder = Folder.objects.create(
                parent = data['parent'],
                name = data['name'],
                owner = request.user.kropboxuser)
            return render(request, 'success.html')
        else:
            form = Add_Folder
          
        return render(request, self.html, {'form':form})

#this is a test
class FileView(View):
    file_form = Add_File
    initial = {'key': 'value'}
    html = 'fileform.html'


    def get(self, request, *args, **kwargs):
        form = self.file_form(request.user.kropboxuser, initial=self.initial)
        return render(request, self.html, {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = self.file_form(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            file_object = FileObject.objects.create(
                folder = data['folder'],
                name = data['name'],
                document = request.FILES['document'])
            return render(request, 'success.html')
        else:
            form = Add_File
        return render(request, self.html, {'form':form})

def success_view(request):
    return render(request, 'success.html')