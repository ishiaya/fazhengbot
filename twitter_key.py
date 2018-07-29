# coding:utf-8

import tweepy

# 各種キーをセット
Consumer_key = '[Consumer_key]'
Consumer_secret = '[Consumer_secret]'
Access_token = '[Access_token]'
Access_secret = '[Access_secret]'

auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
auth.set_access_token(Access_token, Access_secret)

api = tweepy.API(auth)

print('ok')
