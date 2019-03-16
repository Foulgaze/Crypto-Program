
# coding: utf-8

# In[ ]:


import praw
import matplotlib.pyplot as plt
from coinmarketcap import Market
coinmarketcap = Market()
word_list = []
combined_list = {}
#Name is Lukas Veronika
reddit = praw.Reddit(client_id='//client id',
                     client_secret='//secret',
                     password='//not on github',
                     user_agent='Checking for Trending Posts on R/cryptocurrency  /u/CryptoTrendBot',
                     username='CryptoTrendBot')

for submission in reddit.subreddit('Cryptocurrency').hot(limit=1000):
     for word in submission.title.lower().split(' '):
            word_list.append(word)
everything = coinmarketcap.ticker(limit=200)
a = 0
rlong_hands = {}
rshort_hands = {}
rmakes_sense = {}
while a != 100:
    rtemp = everything[a]['name'].lower()
    rtemp2 = everything[a]['symbol'].lower()
    rlong_hands[everything[a]['name'].lower()] = 0
    rshort_hands[everything[a]['symbol'].lower()] = 0
    rmakes_sense[rtemp] = rtemp2
    a += 1
b = 0 
rprices = {}
while b != 100:
    rprices[everything[b]['name'].lower()] = everything[b]['price_usd']
    b += 1 
for item in word_list:        
    for currency in rlong_hands:
        if item == currency:
             rlong_hands[item] += 1
for item in word_list:        
    for currency in rshort_hands:
        if item == currency:
             rshort_hands[item] += 1
for item in rshort_hands:
    for crypto in rmakes_sense:
        if item == rmakes_sense[crypto]:
            rlong_hands[crypto] += rshort_hands[item]
long_percent = rlong_hands
long_names = list(rlong_hands.keys())
for item in long_names:
    if long_percent[item] < 1:
        del long_percent[item]
total = sum(long_percent.values())
length = len(long_percent)



for item in range(length):
    temp = max(long_percent, key=long_percent.get)
    print(temp)
    temp2 = round((long_percent[temp]/total)*100, 1)
    print(str(temp2) + "%")
    del long_percent[temp]

