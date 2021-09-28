#!/usr/bin/python3
"""
This module defines the following function:
    top_ten(subreddit)
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit
    """
    url = "https://www.reddit.com/r/{}/.json?limit=10".format(subreddit)
    headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64)\
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61\
               Safari/537.36"}

    response = requests.get(url, headers=headers).json()
    response = response.get('data').get('children')

    for post in response:
        title = post.get('data').get('title')
        print(title)
