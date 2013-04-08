from django.db import models

class User(models.Model):
    name = models.CharField(max_length=250) 
    sex = models.IntegerField(default=None,null=True)
    age = models.IntegerField(default=None,null=True)
    city = models.IntegerField(default=None,null=True)
    follower = list()
    following = list()
    created_at = models.DatetimeField()
    
    
