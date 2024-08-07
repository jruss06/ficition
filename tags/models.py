from django.db import models

from story.models import Story

class Tag(models.Model):
    name = models.CharField(max_length=200)
    added_date = models.DateTimeField("date added", auto_now_add=True)
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    def __str__(self):
        return self.name