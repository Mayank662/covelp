from django.shortcuts import render
from django.http import HttpResponse

from tweepy import *
import tweepy
import re 
import string
import preprocessor as p

# Create your views here.
def home(request):
    return render(request, 'home.html')

def search(request):
    consumer_key = 'z18WrER64TXmSgHOLijYhu8oj'
    consumer_secret = 'TITG51MsArRqRXQ49g5U8nUDI4yb8M9oPhBM0qbTiM7AodYdyp'
    access_key = '1354434577096445953-QMdZip0jp4DB37Ma6QHx1r24IGUES8'
    access_secret = '4QWNI0719wojkDAOV3BPaZEkXY46q08CphcaVG0EON4jp'

    # Pass your twitter credentials to tweepy via its OAuthHandler
 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
 
    api = tweepy.API(auth,wait_on_rate_limit=True)
 
    search_words = "covid+helpline"      # enter your words
    new_search = search_words + " -filter:retweets"

    obj = tweepy.Cursor(api.search, q=new_search, count=100, lang='en', since_id=0).items(100)


    date = []
    content = []
    name = []
    location = []
    link = []
    for tweet in obj:
	    date.append(tweet.created_at)
	    content.append(tweet.text.encode('utf-8'))
	    name.append(tweet.user.screen_name.encode('utf-8'))
	    location.append(tweet.user.location.encode('utf-8'))
	    link.append(re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet.text))
	
    data=[]
    data.append(date)
    data.append(content)
    data.append(name)
    data.append(location)
    data.append(link)
    return render(request, 'result.html', {'data':data})