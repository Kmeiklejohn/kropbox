from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class KropboxUser(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    username = models.CharField(max_length=124)

    def __str__(self):
        return self.user.username

class Submission(models.Model):
    author = models.ForeignKey(
        KropboxUser,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=250)
    url = models.CharField(max_length=250)
    submitTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.author.user.username

    class Meta:
        ordering = ('-submitTime',)
