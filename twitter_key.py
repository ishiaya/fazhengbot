# coding:utf-8

import tweepy, os

# 各種キーをセット
Consumer_key = os.environ["Consumer_key"]
Consumer_secret = os.environ["Consumer_secret"]
Access_token = os.environ["Access_token"]
Access_secret = os.environ["Access_secret"]

auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
auth.set_access_token(Access_token, Access_secret)

api = tweepy.API(auth)

print('ok')
