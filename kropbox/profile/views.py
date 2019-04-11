from django.shortcuts import render, HttpResponseRedirect, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import reverse 
from kropbox.profile.models import KropboxUser
from kropbox.profile.forms import SignupForm, LoginForm
from kropbox.manager.models import Folder, FileObject

def signup_view(request):
    html = 'genericForm.html'
    form = None

    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                email=data['email'],
                username=data['username'],
                password=data['password'])
            login(request, user)
            kropuser = KropboxUser.objects.create(
                name=data['name'],
                user=user
            )
            Folder.objects.create(
                name = "home",
                owner = kropuser
            )
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = SignupForm()
    return render(request, html , {'form': form})


def login_view(request):
    html = 'genericForm.html'
   
    if request.method == "POST":
    
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('profile'))
    else:
        form = LoginForm()
    return render(request, html, {'form': form})

def logout_view(request):

    logout(request)
    return HttpResponseRedirect(request.GET.get('next', '/'))

def home_view(request):
    
    return render(request, 'home.html')

@login_required()
def profile_view(request):
    user = request.user
    user_id = request.user.id
    kropbox_user = request.user.kropboxuser.name
    folder_list = Folder.objects.all()
    myfolder_list = Folder.objects.filter(owner=request.user.kropboxuser)
    object_list = FileObject.objects.all()
    myitem_list = []
    structure={}
    


    for item in myfolder_list:
        myitem = FileObject.objects.filter(folder=item)
        myitem_list.append(myitem)
    myfiles = []
    for folder in myfolder_list:
        myfiles.append(folder.get_children)
    descendantfiles = []
    for folder in myfolder_list:
        descendantfiles.append(folder.get_descendants(include_self=False))
    descendantfiles2 = []
    for folder in myfolder_list:
        descendantfiles2.append(folder.get_descendants(include_self=True))
    myobjects = []
    for file in myfiles:
        # myobjects.append(file.get_children)
        myobjects.append(file)

    context = {
        'KropboxUser': KropboxUser,
        'user': user,
        'user_id': user_id,
        'kropbox_user': kropbox_user,
        'folder_list': folder_list,
        'myfolder_list': myfolder_list,
        'object_list': object_list,
        # 'myobject_list': myobject_list,
        'myfiles': myfiles,
        'descendantfiles': descendantfiles,
        'descendantfiles2': descendantfiles2,
        'myobjects': myobjects,
        'myitem_list': myitem_list,
    }
    return render(request, 'profile.html', context)

def success_view(request):
    return render(request, 'success.html')