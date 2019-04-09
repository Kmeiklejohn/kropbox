from django.urls import path
from kropbox.manager.views import ManagerView

urlpatterns = [
    path('add_folder/', ManagerView.as_view()),
]