# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 13:11:39 2021

@author: Ryan
"""


# -*- coding: utf-8 -*-
"""
First attempt at Reddit scraper for training facial recognition to grab
looks-like pics for ultimate degeneracy.

Update: holy shit, it works! Need to add spread of subreddits. Likely doesn't 
make sense to download everything and then parse the downloads, but I have to
see whether a facial recognition algo can direct the scraping...

Created on Tue Jan 26 12:32:34 2021

@author: Ryan
"""

import praw
import os
import json
import requests
import wget


reddit = praw.Reddit(client_id='9PGIAT2OrQvsVQ',
                     client_secret = '4ldxeQUyQgOIinRn4-g6ZfwSD-gPfA',
                     user_agent = 'deep-learning-collector')
os.chdir("F:/Photo_scraping_repo")

sub = ['Rateme']

checkWords = ['i.imgur.com',  'jpg', 'png', 'webm',] #'gif', 'gfycat.com',]
already_done = []

for s in sub:

    subreddit = reddit.subreddit(s)
    posts = subreddit.new(limit=10)

    for post in posts:
       
        #print(post.title)
        print(post.url)
        #image_urls.append(post.url.encode('utf-8'))
        #image_titles.append(post.title.encode('utf-8'))
        #image_scores.append(post.score)
        #image_timestamps.append(datetime.datetime.fromtimestamp(post.created))
        #image_ids.append(post.id)
    
        #resp = requests.get(post.url)
        #resp.raise_for_status()
    
        url_text = post.url
        has_domain = any(string in url_text for string in checkWords)
        #print '[LOG] Getting url:  ' + url_text
        #is_gifcat = any(string in url_text for string in gyfwords)
        if post.id not in already_done and has_domain:
           #if is_gifcat:
              #url = re.sub('http://.*gfycat.com/', '', url_text)
              #url_text = 'http://giant.gfycat.com/' + url + '.gif' 
          #wget.download(url_text, '/home/ieuang/Pictures/Extra/' + str(time.time())[-8:-3] + url_text[-4:])
           wget.download(url_text)
           already_done.append(post.id)
           #print '[LOG] Done Getting ' + url_text