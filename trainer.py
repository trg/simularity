from brain import Brain

from twitter import * # https://github.com/sixohsix/twitter

import json
import os

OAUTH_TOKEN = os.getenv('OAUTH_TOKEN')
OAUTH_SECRET = os.getenv('OAUTH_SECRET')
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')

auth = OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_stream = TwitterStream(auth=auth)
iterator = twitter_stream.statuses.sample()

brain = Brain()

for tweet in iterator:
    if tweet.has_key('entities') and tweet['entities'].has_key('hashtags'):
        hashtags = tweet['entities']['hashtags']
        hashtag_list = [ht['text'].encode('utf-8').lower() for ht in hashtags if len(ht) > 1]
        if len(hashtag_list) > 0:
            print hashtag_list
            brain.learn(hashtag_list)

