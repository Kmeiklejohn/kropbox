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
                data['username'],
                data['email'],
                data['password'])
            login(request, user)
            kropuser = KropboxUser.objects.create(
                username=data['name'],
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
    html = 'login.html'
    form = None

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate( username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', 'profile/'))
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
    user2 = request.user.kropboxuser
    kropbox_user = KropboxUser.username
    folder_list = Folder.objects.all()
    object_list = FileObject.objects.all()
    # folder_o bject_list"""

    context = {
        'KropboxUser': KropboxUser,
        'user': user,
        'user_id': user_id,
        'user2': user2,
        'kropbox_user': kropbox_user,
        'folder_list': folder_list,
        'object_list': object_list,
    }
    return render(request, 'profile.html', context)
