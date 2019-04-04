from django.db import models
from mptt.models import MPTTModels, TreeForeignKey


class FileObject(MPTTModel):
	parent = TreeForeignkey('self', related_name='children', null=True, blank=True)
	name = models.CharField()
	file_type = models.CharField(Choices=(('file', 'file'), ('folder', 'folder')))
	encoding = models.CharField(blank=True, null=True)
    
