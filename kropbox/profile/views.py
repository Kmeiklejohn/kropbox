from django.shortcuts import render, HttpResponseRedirect, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import reverse 
from kropbox.profile.models import KropboxUser
from kropbox.profile.forms import SignupForm, LoginForm

def signup_view(request):
    html = 'genericForm.html'
    form = None

    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data['username'],
                password=data['password'],
                email=data['email']
            )
            login(request, user)
            KropboxUser.objects.create(
                user=user,
            )
            return HttpResponseRedirect(reverse('home'))
    else:
        form = SignupForm()
    return render(request, html, {'form': form})

def login_view(request):
    html = 'login.html'
    form = None

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'],
                password=data['password']
            )
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', '/'))
    else:
        form = LoginForm()
    return render(request, html, {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")

def home_view(request):
    items = KropboxUser.objects.all()
    currentUser = request.user

    context = {
        'data':items,
        'currentUser':currentUser
    }
    return render(request, 'home.html', context)

@login_required()
def profile_view(request, KropboxUser_id):
    user = request.user
    user_id = request.user.id
    user2 = request.user.kropboxuser
    KropboxUser = KropboxUser
    kropbox_user = KropboxUser.username
    kropbox_user_id = kropbox_user_id.id
    KropboxUser_id = KropboxUser.id
    selected_user = get_object_or_404(KropboxUser, pk=KropboxUser_id)
    selected_username= selected_user.username
    user_list = KropboxUser.objects.all()
    allstuff = KropboxUser.objects.get(id=KropboxUser_id)
    folder_list = Folder.objects.all()
    user_list = Folder.objects.all().filter(id=user.id)

    context = {
        'user': user,
        'user_id': user_id,
        'user2': user2,
        'KropboxUser': KropboxUser,
        'kropbox_user': kropbox_user,
        'kropbox_user_id': kropbox_user_id,
        'KropboxUser_id': KropboxUser_id,
        'selected_user': selected_user,
        'selected_username': selected_username,
        'folder_list': folder_list,
        'allstuff': allstuff,
        'user_list': user_list,
    }
    return render(request, 'profile.html', context)
