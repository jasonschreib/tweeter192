from django.shortcuts import render

# Create your views here.

#splash page view
#take in request and render the splash.html template
def splash(request):
  return render(request, 'splash.html', {})

#log in and sign up page view
def login(request):
  return render(request, 'login.html', {})

#home page view - all tweets and hashtags


#profile page view - specific users tweets


#hashtag page view - all tweets that correspond to a hashtag