#web_app/services/twitter_service.py

import os
import tweepy

from dotenv import load_dotenv

load_dotenv()

TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")


auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
print("AUTH", type(auth))

api = tweepy.API(auth)
print("API CLIENT", type(api))

user = api.get_user("s2t2")
print(type(user)) #> <class 'tweepy.models.User'>

from pprint import pprint
pprint(user._json)
print(user.id)
print(user.screen_name)
print(user.name)
print(user.followers_count)


breakpoint()