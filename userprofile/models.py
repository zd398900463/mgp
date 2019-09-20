from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    realname = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    # avatar = models.ImageField(upload_to='avatar/%Y-%m-%d', blank=True)

    def __str__(self):
        return 'user {}'.format(self.user.username)
