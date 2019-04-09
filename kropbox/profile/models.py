from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class KropboxUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.name


