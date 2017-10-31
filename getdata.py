#!/usr/bin/python2.7


import twitter
import tweepy
import os

"""
Setting up the auth parameters for using the tweepy module on twitter application created with OAuth.
Twitter username - @e_purohit

Example:

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
"""

auth = tweepy.OAuthHandler("v22l2KMtXLJY3ZTiEpNyRyLUj", "2GCvf1ul33i0eyGyNq6Uo6oWeSL4gmUfyghnlFKHxMU9D0SyuL")
auth.set_access_token("887755823522340865-8F9qeIWfm6fzYPpI4mJVXXq1iuFgCcm", "VgLvgj015uajs3vzHdX3vSi3jIPNfZP03flzI7CIjOtqk")

api = tweepy.API(auth)

for status in tweepy.Cursor(api.search, q="happy",tweet_mode="extended", since_id=100, count=100).items(100):
    # process status here
    print status.entities["hashtags"]
    print status.full_text

"""
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
"""
