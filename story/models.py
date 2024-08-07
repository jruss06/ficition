from django.db import models
from django.contrib.auth.models import User

from tags.models import Tag

class Story(models.Model):
    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=1000)
    added_date = models.DateTimeField("date added", auto_now_add=True)
    update_date = models.DateTimeField("date updated", auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.title


class Chapter(models.Model):
    title = models.CharField(max_length=200)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    body = models.TextField()
    order = models.IntegerField()
    added_date = models.DateTimeField("date added", auto_now_add=True)
    update_date = models.DateTimeField("date updated", auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
