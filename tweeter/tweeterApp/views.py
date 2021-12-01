from django.shortcuts import render, redirect
#import the tweet class, hashtag class
from tweeterApp.models import Tweet
# , hashtag
#import authentication and login methods
from django.contrib.auth import authenticate, login

# Create your views here.

#splash page view
#take in request and render the splash.html template
def splash(request):
  return render(request, 'splash.html', {})

#accounts page view - to signup or login
def accounts(request):
  return render(request, 'accounts.html', {})

#sign up page view - will always redirect to either accounts (if can't go through) or home
def signup(request):
  return render(request, 'accounts.html', {})

#log in page view - will always redirect to either accounts (if can't go through) or home
def login_view(request):
  #if we are making a post request --> creating a new session
  if (request.method == 'POST'):
    #get username and password
    username, password = request.POST['username'], request.POST['password']
    #authenticate the user
    user = authenticate(username=username, password=password)
    #if the user is not authenticated
    if (user is None):
      #return back to the login page
      return redirect('/accounts')
    #otherwise if the user is a user
    else:
      #login the user
      login(request, user)
      #redirect to homepage
      return redirect('/home')
  # return render(request, 'accounts.html', {})

#home page view - all tweets and hashtags
def home(request):
  print('hey')
  #if the request is a POST request - meaning new tweet
  if (request.method == 'POST'):
    print('REQ', request.POST)
    #retrieve data from the post req
    body = request.POST['body']
    #create a new tweet for the database
    Tweet.objects.create(body=body, author=request.user)
  #if the request is a PATCH request - meaning a user liked a post
  # if (request.method == 'PATCH'):
  print('PATCHHHH', request.method)
    #update the likes on the post by one
  #retrieve all instances of the tweet class
  tweets = Tweet.objects.all()
  return render(request, 'home.html', {"tweets": tweets}) #want to pass in all the tweets, do we need to pass in the user?

#profile page view - specific users tweets
def profile(request):
  return render(request, 'profile.html', {}) #want to pass in the user - and get the user's tweets

#hashtag page view - all tweets that correspond to a hashtag
def hashtag(request):
  return render(request, 'hashtag.html', {}) #want to pass in the hashtag - and get all the tweets that use the hashtag