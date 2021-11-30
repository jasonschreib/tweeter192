from django.shortcuts import render
#import the tweet class, hashtag class
from tweeterApp.models import tweet, hashtag

# Create your views here.

#splash page view
#take in request and render the splash.html template
def splash(request):
  return render(request, 'splash.html', {})

#log in and sign up page view
def login(request):
  return render(request, 'login.html', {})

#home page view - all tweets and hashtags
def home(request):
  #retrieve all instances of the tweet class
  tweets = tweet.objects.all()
  return render(request, 'home.html', {"tweets": tweets}) #want to pass in all the tweets, do we need to pass in the user?

#profile page view - specific users tweets
def profile(request):
  return render(request, 'profile.html', {}) #want to pass in the user - and get the user's tweets

#hashtag page view - all tweets that correspond to a hashtag
def hashtag(request):
  return render(request, 'hashtag.html', {}) #want to pass in the hashtag - and get all the tweets that use the hashtag