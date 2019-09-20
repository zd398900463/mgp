from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class DataSource(models.Model):
    screen_name = models.CharField(blank=True, max_length=15)
    reposts_count = models.PositiveIntegerField(blank=True)
    comments_count = models.PositiveIntegerField(blank=True)
    attitudes_count = models.PositiveIntegerField(blank=True)
    followers_count = models.PositiveIntegerField(blank=True)
    verified_type = models.IntegerField(blank=True)
    source = models.CharField(max_length=10)

    class Meta:
        ordering = ('-source',)

    def __str__(self):
        # return self.title 将文章标题返回
        return str(self.source)

class DataShow(models.Model):
    dtitle = models.CharField(blank=True, max_length=150)
    dcontent = models.TextField()
    dsource = models.ForeignKey(DataSource, on_delete=models.CASCADE)
    disposition = models.NullBooleanField(blank=True)
    dcreated = models.DateTimeField(default=timezone.now)
    dupdate = models.DateTimeField(auto_now=True)
    dclass = models.CharField(blank=True, max_length=150)
    durl = models.URLField(blank=True)

    class Meta:
        ordering = ('-dcreated',)

    def __str__(self):
        # return self.title 将文章标题返回
        return self.dtitle


