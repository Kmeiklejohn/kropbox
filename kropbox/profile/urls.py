from django.urls import path

from kropbox.profile.views import home_view, signup_view, login_view, profile_view, logout_view, success_view, document_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view, name="index"),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('profile/<int:id>', folder_view, name='folder_view'),
    path('logout/', logout_view, name='logout'),
    path('success/', success_view, name='success'),
    path('document/<int:fileobject_id>', document_view, name='document')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


