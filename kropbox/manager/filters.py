from kropbox.manager.models import Folder
from django_filters import Filterset

class UserFilter(FilterSet):
    class Meta:
        model = Folder
        fields = ['parent', 'name', 'owner','created_at' ]