#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 13:39:36 2020

@author: ayakanakatsuka
"""

#importing Tweepy
pip install git+https://github.com/tweepy/tweepy.git
import tweepy
import json
API_key=""
API_secret=""
access_token_secret=""
access_token=""

auth = tweepy.OAuthHandler(API_key, API_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

#Check what kind of tweets there are with #Blacklivesmatter movement
search_words = "#blacklivesmatter"
date_since = "2020-05-30"
tweets = tweepy.Cursor(api.search,q=search_words,lang="en",since=date_since).items(5)
for tweet in tweets:
    print(tweet.text)

#Analyze the sentiment of Blacklivesmatter movement
query = '#blacklivesmatter'
max_tweets = 10000
searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]

pip install -U textblob
from textblob import TextBlob
pos = 0
neg = 0
neu = 0
for tweet in searched_tweets:
    analysis = TextBlob(tweet.text)
    if analysis.sentiment[0]>0:
       pos = pos +1
    elif analysis.sentiment[0]<0:
       neg = neg + 1
    else:
       neu = neu + 1

sentiment_data={'Positive':pos,'Negative':neg,'Neutral':neu}
import matplotlib.pyplot as plt
fig,ax=plt.subplots()
ax.pie(values,labels=names,autopct='%.2f')
plt.show

#Convert json to pandas
my_demo_list = []
with open('tweet_blacklivesmatter.txt', encoding='utf-8') as json_file:
    all_data = json.load(json_file)
    for each_dictionary in all_data:
        tweet_id = each_dictionary['id']
        text = each_dictionary['text']
        favorite_count = each_dictionary['favorite_count']
        retweet_count = each_dictionary['retweet_count']
        created_at = each_dictionary['created_at']
        geo = each_dictionary['geo']
        my_demo_list.append({'tweet_id': str(tweet_id),
                            'text': str(text),
                            'favorite_count': int(favorite_count),
                            'retweet_count': int(retweet_count),
                            'created_at':created_at,
                            'geo':str(geo),'lang':str(lang)})

tweet_json = pd.DataFrame(my_demo_list, columns =
                                 ['tweet_id', 'text',
                                  'favorite_count', 'retweet_count',
                                  'created_at','geo','lang'])

#maybe add entities -->hashtag, user-->location ,lang
#Top 5 languages
tweet_json['lang'].value_counts()[0:5]
