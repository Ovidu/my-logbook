from django.db import models
from django.utils import timezone
from django import forms


BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))
class Post(models.Model):
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)

class MyModel(models.Model):
    completed = models.BooleanField(choices=BOOL_CHOICES)

    def publish(self):
        self.published_date = timezone.now()
        self.save
    def __str__(self):
        return self.title
