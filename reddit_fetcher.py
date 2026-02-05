import praw
import os

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="reddit_analyzing_agent"
)

subreddit = reddit.subreddit("stocks")
for post in subreddit.hot(limit=5):
    print(post.title)
