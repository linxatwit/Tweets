from flask import Flask, render_template, request
from flask_cors import CORS
from models import create_post, get_posts, delete_posts

app = Flask(__name__)

CORS(app)

from tweepy import OAuthHandler
import tweepy

import twitter_credentials

import json

@app.route('/', methods=['GET', 'POST'])

def index():
    jsonfile = open("tweets.json", "w")
    list_of_json = []

    auth = OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
    auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)

    #API object
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    
    if request.method == 'GET':
        delete_posts()

    if request.method == 'POST':
        delete_posts()
        tweetid = ''
        tweetContent = ''
        post = request.form.get('post')
        for tweet in api.search(q=post, tweet_mode='extended'):
            tweetid = tweet.id
            tweetContent = tweet.full_text
            create_post(tweetid, tweetContent)
            list_of_json.append(tweet)
            #print(f'{tweet.id}:{tweet.full_text}')     

    posts = get_posts()
    for jsonTweet in list_of_json:
        json.dump(jsonTweet._json, jsonfile)

    return render_template('submit.html', title='submit', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)