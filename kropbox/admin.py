from kropbox.manager.models import Folder, FileObject
from kropbox.profile.models import KropboxUser
from django_mptt_admin.admin import DjangoMpttAdmin
from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin


admin.site.register(KropboxUser)
admin.site.register(FileObject)
admin.site.register(
    Folder,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)
