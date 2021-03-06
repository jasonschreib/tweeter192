"""tweeter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#import all views from views.py
from tweeterApp.views import splash, accounts, signup, login_view, home, delete, like, dislike, profile, hashtag, logout_view
#import the tweet class, hashtag class
from tweeterApp.models import Tweet, Hashtag

urlpatterns = [
    path('admin/', admin.site.urls),
    #url for the splash page
    path('', splash, name='splash'),
    #url for the accounts page
    path('accounts', accounts, name='accounts'),
    #url for the signup (which will then redirect)
    path('signup', signup, name='signup'),
    #url for the login (which will then redirect)
    path('login', login_view, name='login_view'),
    #url for the home page
    path('home', home, name='home'),
    #url for deleting a tweet (which will then redirect to home)
    path('delete', delete, name='delete'),
    #url for liking a tweet (which will then redirect to home)
    path('like', like, name='like'),
    #url for disliking a tweet (which will then redirect to home)
    path('dislike', dislike, name='dislike'),
    #url for a user's profile of tweets
    path('profile', profile, name='profile'),
    #url for a hashtag's tweets
    path('hashtag', hashtag, name='hashtag'),
    #url for the logout (which will then redirect to accounts)
    path('logout', logout_view, name='logout_view')
]
