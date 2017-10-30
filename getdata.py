#!/usr/bin/python2.7


import twitter
import os


api = twitter.Api(consumer_key ="v22l2KMtXLJY3ZTiEpNyRyLUj",
                  consumer_secret="2GCvf1ul33i0eyGyNq6Uo6oWeSL4gmUfyghnlFKHxMU9D0SyuL",
                  access_token_key="887755823522340865-8F9qeIWfm6fzYPpI4mJVXXq1iuFgCcm",
                  access_token_secret="VgLvgj015uajs3vzHdX3vSi3jIPNfZP03flzI7CIjOtqk")

results = api.GetSearch(
    raw_query="l=&q=terror&count=100")


for i in range(len(results)):
	print results[i].text