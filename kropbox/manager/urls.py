from django.urls import path
from kropbox.manager.views import FolderView, FileView

urlpatterns = [
    path('add_folder/', FolderView.as_view()),
    path('add_file/', FileView.as_view()),
]