import dotenv
from dotenv import load_dotenv
import os

load_dotenv()

#
import tweepy
import requests

consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')
bearer_token = os.environ.get('BEARER_TOKEN')
#print('CONSUMER_KEY',consumer_key)
#print('BEARER_TOKEN',bearer_token)
#print('ACCESS_TOKEN_SECRET',access_token_secret)
#print('ACCESS_TOKEN',access_token)
#print('CONSUMER_SECRET',consumer_secret)

# your app code here

client = tweepy.Client(bearer_token=bearer_token,
consumer_key=consumer_key,
consumer_secret=consumer_secret,
access_token=access_token,
access_token_secret=access_token_secret,
return_type = requests.Response,
wait_on_rate_limit=True)
print('OK')

# Define query
query = '#100daysofcode (pandas OR python) -is:retweet'

# get max. 100 tweets
tweets = client.search_recent_tweets(query=query, tweet_fields=['author_id','created_at','lang'],max_results=100)

print('tweets',tweets.status_code)

print(tweets.text)

import pandas as pd

# Save data as dictionary
tweets_dict = tweets.json() 
#print(type(tweets_dict))

#Extract "data" value from dictionary
tweets_data = tweets_dict['data']


# Transform to pandas Dataframe
tweets_1 = pd.json_normalize(tweets_data)
print(tweets_1)
#5. Take a look at the dataframe to make sure is correct `df.head()`
tweets_1.head(10)

#6. Save the data as a CSV file named coding-tweets.csv

tweets_1.to_csv("tweets_data.csv")

# Step  7

#Now that you have your DataFrame of tweets set up, you're going to do a bit of text analysis 
# to count how many tweets contain the words 'pandas', and 'python'. Define the following function word_in_text(), 
# which will tell you whether the first argument (a word) occurs within the 2nd argument (a tweet). 

import re

def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)

    if match:
        return True
    return False

# Step 8 Iterate through dataframe rows counting 
# the number of tweets in which pandas and python are mentioned, using your word_in_text() function.

[pandas, python] = [0, 0]

for index, row in tweets_1.iterrows():
    pandas += word_in_text('pandas', row['text'])
    python += word_in_text('python', row['text'])

print(pandas)
print(python)


# Step 9 Visualize the data

import matplotlib.pyplot as plt

palabras = ['pandas','python']
print(palabras)
frecuencias = [pandas,python]
print(frecuencias)

# Intento 1
#import seaborn as sns
#sns.countplot(x=palabras, data=frecuencias)

#intento 2
plt.bar(palabras,frecuencias)
plt.title('Frecuencias encontradas en el texto')
plt.xlabel('Palabras')
plt.ylabel('# de veces')
plt.show()

#Intento  3
#1. Import packages
#import matplotlib.pyplot as plt
#import seaborn as sns
#2. Set seaborn style
#sns.set(color_codes=True)


#3. Create a list of labels:cd
#cd = ['pandas','python']
#print(cd)

#4. Plot the bar chart
#x = cd
#data = [pandas, python]
#bar_chart = sns.barplot(cd, data)
#bar_chart.set(ylabel="count")
#plt.show()


