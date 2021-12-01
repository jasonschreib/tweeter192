from django.contrib import admin
#import tweet and hastag models
from tweeterApp.models import Tweet, Hashtag

# Register your models here.
admin.site.register(Tweet)
admin.site.register(Hashtag)