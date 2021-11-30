from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#model for tweets
class Tweet(models.Model):
  body = models.TextField()
  timestamp = models.DateTimeField(auto_now = True)
  author = models.ForeignKey(User, on_delete = models.DO_NOTHING)
  likes = models.IntegerField(default = 0)


#model for hashtags
#class Hashtags(models.Model);