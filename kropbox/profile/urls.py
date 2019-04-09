from django.urls import path
from kropbox.profile.views import home_view, signup_view, login_view, profile_view, logout_view

urlpatterns = [
    path('', home_view, name="index"),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout')
]