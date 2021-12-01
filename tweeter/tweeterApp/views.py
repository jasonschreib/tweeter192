from django.shortcuts import render, redirect
#import the tweet class, hashtag class
from tweeterApp.models import Tweet
# , hashtag
#import authentication and login methods
from django.contrib.auth import authenticate, login, logout
#import the User object
from django.contrib.auth.models import User

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
  #if the request is POST
  if (request.method == 'POST'):
    #get the username, email, and password from the request
    username, email, password = request.POST['username'], request.POST['email'], request.POST['password']
    #create a user with the username and password
    user = User.objects.create_user(username=username, email=email, password=password)
    #login the user
    login(request, user)
    #return a redirect to homepage
    return redirect('/home')


#log in page view - will always redirect to either accounts (if can't go through) or home
def login_view(request):
  #if the user is authenticated
  if (request.user.is_authenticated):
    #bring them to the homepage
    return redirect('home')
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
  #get the author from the request
  print(request.GET.get('q'))
  return render(request, 'profile.html', {"author": author}) #want to pass in the user - and get the user's tweets


#hashtag page view - all tweets that correspond to a hashtag
def hashtag(request):
  return render(request, 'hashtag.html', {}) #want to pass in the hashtag - and get all the tweets that use the hashtag


#logout page view - will logout user and redirect to the accounts page
def logout_view(request):
  logout(request)
  return redirect('accounts')