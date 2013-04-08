from django.db import models
from user import User

class Topic(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    contenttype = models.FoerignKey('ContentType')
    owner = models.FoerignKey('User')
    follower = list()
    watched = models.IntegerField()
    

class ContentType(models.Model):
    name = models.CharField(max_length=255)
