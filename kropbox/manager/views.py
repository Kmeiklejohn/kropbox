from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from kropbox.manager.models import FileObject, Folder
from kropbox.manager.forms import Add_File, Add_Folder
from django.views import View

class ManagerView(View):
    folder_form = Add_Folder()
    file_form = Add_File()
    initial = {'key': 'value'}
    html = 'genericForm.html'


    def get_folder(self, request):
        form = self.folder_form(initial=self.initial)
        return render(request, self.html, {'form':form})

    def add_folder(self, request):
        form = self.folder_form(request.POST)
        if form.valid():
            data = form.cleaned_data
            folder = Folder.objects.create(
                name = data['name'],
                owner = data['username'],
                parent = data['parent']
            )
            pass

