from django.urls import path
from kropbox.manager.views import ManagerView

urlpatterns = [
    path('manager/', ManagerView.as_view()),
]