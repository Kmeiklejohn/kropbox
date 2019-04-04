from django.db import models
from mptt.models import MPTTModels, TreeForeignKey
from kropbox.profile import KropboxUser
class Folder(MPTTModel):
	parent = TreeForeignkey('self', related_name='children', null=True, blank=True)
	name = models.CharField()
	folder_type = models.CharField()
	owner = models.ForeignKey(KropboxUser, on_delete=models.CASCADE)

class FileObject(models.Model):
	folder = TreeForeingKey(Folder)
	name = models.CharField()
	encoding = models.CharField()
	
