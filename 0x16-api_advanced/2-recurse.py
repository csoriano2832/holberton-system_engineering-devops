#!/usr/bin/python3
"""
This module defines the following function:
    recurse(subreddit, hot_list=[])
"""
import requests


def recurse(subreddit, hot_list=[], next_page=None):
    """
    Queries the Reddit API and returns a list containing the titles of all
    hot articles for a given subreddit. If no results are found for the given
    subreddit, the function should return None.
    """
    url = "https://www.reddit.com/r/{}/.json".format(subreddit)
    headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64)\
               AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61\
               Safari/537.36"}
    parameters = {'after': next_page, 'limit': '100'}

    response = requests.get(url, headers=headers, params=parameters)

    if response.status_code == 200:
        response = response.json().get('data')

        hot_list.extend(response.get('children'))
        next_page = response.get('after')

        if next_page is not None:
            recurse(subreddit, hot_list, next_page)
        return hot_list

    else:
        return None
