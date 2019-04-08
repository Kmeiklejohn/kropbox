from django.urls import path
from kropbox.profile.views import home_view, signup_view, login_view 

urlpatterns = [
    path('', home_view, name="index"),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login')
]