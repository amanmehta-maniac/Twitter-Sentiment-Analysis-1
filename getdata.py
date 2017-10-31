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

file = open("traindata.csv", "a")

search = "sad"
tmode = "extended"
cnt = 100
itemlimit = 1000

for status in tweepy.Cursor(api.search, q=search,tweet_mode=tmode, since_id=1, count=cnt).items(itemlimit):
    # process status here
    #print status.entities["hashtags"]
    tweet = status.full_text
    #f.write()
    print tweet

"""
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
"""
