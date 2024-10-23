#!/usr/bin/python3
"""Script that fetches 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit.
    If not a valid subreddit, prints None."""
    
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(subreddit_url, headers=headers, params={'limit': 10}, allow_redirects=False)

    if response.status_code == 200:
        json_data = response.json()
        posts = json_data.get('data', {}).get('children', [])
        
        if posts:
            for post in posts:
                print(post.get('data', {}).get('title', 'No Title'))
            print("OK")  # Indicate that the subreddit is valid and posts were fetched
        else:
            print("OK")  # Subreddit is valid but no posts are available
    else:
        print(None)
