#!/usr/bin/python2.7


import twitter
import tweepy
import os
import re

from segmenter import Analyzer
from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk import pos_tag
from urllib2 import urlopen

"""
Setting up the auth parameters for using the tweepy module on twitter application created with OAuth.
Twitter username - @e_purohit

Example:

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
"""

def getTestdata():
	auth = tweepy.OAuthHandler("v22l2KMtXLJY3ZTiEpNyRyLUj", "2GCvf1ul33i0eyGyNq6Uo6oWeSL4gmUfyghnlFKHxMU9D0SyuL")
	auth.set_access_token("887755823522340865-8F9qeIWfm6fzYPpI4mJVXXq1iuFgCcm", "VgLvgj015uajs3vzHdX3vSi3jIPNfZP03flzI7CIjOtqk")

	api = tweepy.API(auth)

	search = "90"
	itemlimit = 1

	for status in tweepy.Cursor(api.search, lang="en", q=search,tweet_mode="extended", since_id=1).items(itemlimit):
	    # process status here
	    # print status.entities["hashtags"]

	    if "retweeted_status" in dir(status):
	    	tweet=status.retweeted_status.full_text
	    else:
	    	tweet=status.full_text

	    t1 = Tweet(tweet)
	    print t1.text
"""
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text
"""

class Tweet:
	def __init__(self, ftweet):
		self.text = ftweet
		self.processed = ftweet
		self.tokens = []
		self.hashtags = []
		self.fvec = []

	def __tknize(self):
		
		"""
		Tokenize the tweet text using TweetTokenizer.
		
		'strip_handles' removes Twitter username handles from text if set to True.
		'reduce_len' replaces repeated character sequences of length 3 or greater with sequences of length 3 if set to True.
		"""

		ttkzr = TweetTokenizer(strip_handles=True, reduce_len=True)
		self.tokens = ttkzr.tokenize(self.processed)

	def __removeURL(self):
		newText = re.sub(r"http\S+", "", self.processed, flags=re.MULTILINE)
		self.processed = newText

	def __removeNum(self):
		newText = self.processed.translate("","0123456789")
		self.processed = newText

	def __removeSwords(self):
		stop_words = set(stopwords.words('english'))
		stop_words.update(['.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}'])
		
		"""
		Remove the list creation statement below and uncomment this if you need to stem the tokenized words.

		porter = PorterStemmer()
		self.tokenized = [porter.stem(word) for word in self.tokenized if word.lower() not in stop_words]

		"""

		newtokens = [word for word in self.tokens if word.lower() not in stop_words]
		self.tokens = newtokens

	def __findHashtags(self, segment=True):

		for i, token in enumerate(self.tokens):
			if token[0] == "#":
				self.hashtags.append(token)

		if segment == True:

			segTool = Analyzer("twitter")

			for i, tag in enumerate(self.hashtags):
				text = tag.lstrip('#')
				segmented = segTool.segment(text)
				self.hashtags[i] = segmented

	def processTweet(self, remove_nums=True, remove_swords=True, remove_url=True, seg_hashtags=True):
		if remove_url=True:
			self.__removeURL()
		if remove_nums=True:
			self.__removeNum()

		self.__tknize()
		self.__findHashtags(segment=seg_hashtags)

		if remove_swords=True:
			self.__removeSwords()

	def printer(self):
		print("Full tweet: {!r}\n".format(self.processed))
		print("Tweet after removing URL's and numbers: {!r}\n".format(self.processed))
		print("Final tokens obtained from tweet: {!r}\n".format(self.tokens))
		print("Segmented Hashtags: {!r}\n".format(self.hashtags))
		print("Feature vector for the tweet: {!r}\n".format(self.fvec))

getTestdata()