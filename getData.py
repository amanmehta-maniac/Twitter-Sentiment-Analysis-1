#!/usr/bin/python2.7

import tweepy

from tweet import Tweet

"""
Setting up the auth parameters for using the tweepy module on twitter application created with OAuth.
Twitter username - @e_purohit

Example:

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
"""
Emotions = {"sad":0, "happy":1, "angry":2, "surprise":3}
Polarity = {0:"negative", 1:"positive"}

def getTestdata(search = "*", count=1):
	auth = tweepy.OAuthHandler("v22l2KMtXLJY3ZTiEpNyRyLUj", "2GCvf1ul33i0eyGyNq6Uo6oWeSL4gmUfyghnlFKHxMU9D0SyuL")
	auth.set_access_token("887755823522340865-8F9qeIWfm6fzYPpI4mJVXXq1iuFgCcm", "VgLvgj015uajs3vzHdX3vSi3jIPNfZP03flzI7CIjOtqk")

	api = tweepy.API(auth)

	search = "happy"
	itemlimit = count

	for status in tweepy.Cursor(api.search, lang="en", q=search,tweet_mode="extended", since_id=1).items(itemlimit):
	    # process status here
	    # print status.entities["hashtags"]

	    if "retweeted_status" in dir(status):
	    	tweet=status.retweeted_status.full_text
	    else:
	    	tweet=status.full_text

	    t1 = Tweet(tweet)
	    t1.processTweet()
	    t1.printer()


def getTraindata(bpfile = "./Datasets/Sentiment Analysis Dataset.csv", mpfile = "./Datasets/smileannotationsfinal.csv"):
	mpdata = []
	for line in mpfile:
		tokens = line.split[',']

		labels = tokens[2].split('|')
		label = Emotions[labels[0]]

		t1 = Tweet(tokens[1], label)
		t1.processTweet()	
		mpdata.append(t1)

	return mpdata