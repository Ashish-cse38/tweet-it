from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
# from django.template.context import RequestContext

import tweepy
import sys
import datetime as dt

auth = tweepy.OAuthHandler('oIxGjMvP6ij1FonUnvWWXjAsI', 'BmdHs1ROdutUGZrGE8HlEVCTVnp9r549gjJjZXKGyqWwddJnIy')

auth.set_access_token('1311648282821586945-FGQKwKNdpABZ0c0D8xcC0ptwQkAwy6', 'xmexAASZKcNuD2Z2Ev3c5QXn7pe7pinS2q5nYbsR3hUt8')

api = tweepy.API(auth)
#user = api.get_user('twitter')
#user = sys.argv[1]

tweets_list = []
public_tweets = api.home_timeline()

print("hello")
for tweet in public_tweets:
    if tweet.created_at < dt.datetime.today() and tweet.created_at > (dt.datetime.now()-dt.timedelta(days=7)):
      tweets_list.append(tweet)

def login(request):
    # context = RequestContext(request, {
    #     'request': request, 'user': request.user})
    # return render_to_response('login.html', context_instance=context)
    return render(request, 'login.html', {'tweets':tweets_list})


@login_required(login_url='/')
def home(request):
    return render_to_response(request, 'home.html')


def logout(request):
    auth_logout(request)
    return redirect('/')