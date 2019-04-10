from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from kropbox.profile.models import KropboxUser


class Folder(MPTTModel):
	parent = TreeForeignKey('self', related_name='children', null=True, blank=True, db_index=True ,on_delete=models.CASCADE)
	name = models.CharField(max_length=60)
	owner = models.ForeignKey(KropboxUser, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now_add=True)
	
	class MPTTMeta:
    	 order_insertion_by = ['name']

	def __str__(self):
		return self.name

#help
class FileObject(models.Model):
	folder = TreeForeignKey(Folder, on_delete=models.CASCADE)
	name = models.CharField(max_length=60)
	document = models.FileField(upload_to='documents/%Y/%m/%d')
	created_at = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.name
	
