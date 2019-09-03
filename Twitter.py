import tweepy
from textblob import TextBlob
import csv
import re
import sys
import pandas as pd

consumer_key='F8vEwj77kTfWUwzPhqzGU5In2'
consumer_secret='l0bHse48RhQaGLM0P6HC8esLAFKZOCnyJ4c6MWbP1hsON9k70v'

access_token_key='1168434697787121664-09Dv3fKh64zx0cqsoNZrE2XnbsY1lU'
access_token_secret='qT8k16Ngz0xY2hcDpbrd6N47t6HQproyLdomJG2ssjdGL'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token_key,access_token_secret)

api=tweepy.API(auth)
topicname='Trump'
pubic_tweets=api.search(topicname)
unwanted_words=['@','RT',':','https','http']
symbols=['@','#']
data=[]
for tweet in pubic_tweets:
    text=tweet.text
    textWords=text.split()
    #print (textWords)
    cleanedTweet=' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|(RT)", " ", text).split())
    print (cleanedTweet)
    #print (TextBlob(cleanedTweet).tags)
    analysis= TextBlob(cleanedTweet)
    print(analysis.sentiment)
    polarity = 'Positive'
    if(analysis.sentiment.polarity < 0):
        polarity = 'Negative'
    if(0<=analysis.sentiment.polarity <=0.2):
        polarity = 'Neutral'
    #print (polarity)
    dic={}
    dic['Sentiment']=polarity
    dic['Tweet']=cleanedTweet
    data.append(dic)
df=pd.DataFrame(data)

print(df.head())
df['Sentiment'].hist()

import matplotlib.pyplot as plt
# plt.hist(df['Sentiment'], density=True)
# plt.show()


print(df.group_by())

df.to_csv('analysis1.csv')
