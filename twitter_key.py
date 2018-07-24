# coding:utf-8

import tweepy

# 各種キーをセット
CONSUMER_KEY = '[CONSUMER_KEY]'
CONSUMER_SECRET = '[CONSUMER_SECRET]'
ACCESS_TOKEN = '[ACCESS_TOKEN]'
ACCESS_SECRET = '[ACCESS_SECRET]'

auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
auth.set_access_token(Access_token, Access_secret)

api = tweepy.API(auth)

print('ok')
