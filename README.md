# tweeter192
A simple clone of a treasured social media, Twitter

Documentation of my routes, and design considerations:
    #url for the splash page --> '/'

    #url for the accounts page --> '/accounts'

    #url for the signup (which will then redirect back to homepage if successful) --> '/signup'

    #url for the login (which will then redirect back to homepage if successful) --> '/login'

    #url for the home page --> '/home'

    #url for deleting a tweet (which will then redirect to homepage after deleting the tweet) --> '/delete'

    #url for liking a tweet (which will then redirect to home) --> '/like?id={{tweet.id}}'

    #url for disliking a tweet (which will then redirect to home) --> '/dislike?id={{tweet.id}}'

    #url for a user's profile of tweets --> '/profile?id={{tweet.id}}'

    #url for a hashtag's tweets --> '/hashtag'

    #url for the logout (which will then redirect to accounts page) --> '/logout'


How to run the server:
Django must be installed
Run the following command to create db --> python3 manage.py makemigrations
Then --> python3 manage.py migrate
Then the following to run the server --> python3 manage.py runserver



Introduction
The beauty of web development is its ability to create software that anybody with an internet connection can use. In this assignment, you will implement a clone of my favourite social media - Twitter! An implementation of the website is available here and you are expected to recreate all the functionality from the site. This might seem a little daunting - but I assure you that everything you need to know has been covered in lecture.

In particular, you must be able to sign in and create tweets that support hashtagging (i.e. the tweet “I love #programming in #cis192” contains two hashtags) such that accessing the page for a given hashtag will return the tweets that contain the hashtag. In addition, you must be able to delete tweets (if you are signed in as the author). You also need to create profile pages for each user that display their username and the tweets they wrote (all tweets must be displayed in order of recency). For this assignment, all tweets will be public (in essence, all users follow each other by default).

This assignment is meant to be developed from scratch, including importing packages from the pip registry. Feel free to consult the Django boilerplate code provided in lecture.

Milestone 1: Templates
The recommended approach to developing this application is to start by writing the HTML templates that the application requires. At the very minimum the application requires the following pages:

Log In and Sign Up page(s)
Splash page (explanation of product)
Home page (feed of tweets and hashtags)
Profile page (display of each users tweets)
Hashtag page (display of the tweets that correspond to a hashtag)
You should also write the URLs and views to simply render the templates too, in order to both debug and set up some boilerplate for you to implement in Milestone 3. Be sure to use a CSS framework to keep your web pages production-ready. I like to use Bootstrap or Bulma, but anything that doesn’t use Times New Roman is fair game.

Milestone 2: Accounts System
Once you have a working accounts system, the entire flow of development will be completely different. Django’s authentication system lets us implement this very easily (refer to the lecture notes for more information). It is not necessary to extend the user model (e.g. bio, profile picture etc.), but extra credit will be given where due!

Milestone 3: Model Definitions
The only two models that you need to implement are a Tweet model and a Hashtag model. Be sure to make use of SQL relationships, namely the foreign_key and ManyToMany relationships. In class we've seen foreign keys, in which we relate two objects together. The ManyToMany relationship is an extension of the foreign key, where an object can be associated with a set of relationships to object of the same type (think Facebook posts having a ManyToMany relationship with comments). Read more about it here.

Tweets must contain a timestamp and their associated author. In addition, tweets must supporting the “liking” feature such that each user can like and unlike tweets.

Be sure to create a user using createsuperuser and use the admin page to test out your models before moving onto implementing your views.

HALF WAY POINT (https://www.youtube.com/watch?v=EBZp9IZFdTU)

Milestone 3: Views
It’s time to put everything together and make your application functional! Create the associated views that correspond to the templates and forms that you wrote in your HTML. Think hard about how to parse hashtags in the body of POSTed tweets. Look into regular expressions, or feel free to implement your own string function to identify hashtags.
