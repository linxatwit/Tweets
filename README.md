# Tweets
Python Flask web application that uses Twitter API to collect tweets, save them to the database, and to a JSON file.

## Installation
If Flask isn't installed, install Flask and Flask-CORS.

```pip install flask```
```pip install flask-cors```

If Tweepy isn't installed, install it.

```pip install tweepy```

## SQLite Database
To view the database, download the ```sqlite-tools``` zip file from their downloads page for your respective OS: https://www.sqlite.org/download.html

Upzip the file and open the ```DB Browser for SQLite``` application. To view the database, open the Data Base File by selecting the ```database.md``` file in the project.

## Twitter Credentials
In the ```twitter_credentials.py``` file, replace the empty strings with your Twitter access token and consumer key.

## Run
```python -m flask run```

## Terminate
Ctrl + C to terminate flask application.
