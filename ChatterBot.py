import numpy as np
import tweepy
import time
import json
consumer_key = '0nUJN5UkXWwGOOhx93npeHSNc'
consumer_secret = 'Qd6xbsY0SD0HmI9Z1MwKMvbrvM0w5UHxNVqMFjp0bHDOZAxa1T'
access_token = '979169454876536832-rXIqC5IMNhPuMUw8K1ind5fcQYiTDLW'
access_token_secret = 'yS7IQRKao3esTaKblhRWtXvBqWaFQKobmVbrLUUtRk7ez'
# Target Term
target_term = "@aiyan8732"
print("We're going live!")
def ThankYou():

    # Twitter Credentials
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # Search for all tweets
    public_tweets = api.search(target_term, count=100, result_type="recent")

    # Loop through all tweets
    for tweet in public_tweets["statuses"]:

        # Get ID and Author of most recent tweet directed to me
        tweet_id = tweet["id"]
        tweet_author = tweet["user"]["screen_name"]

        # Print the tweet_id
        print(tweet_id)

        # Use Try-Except to avoid the duplicate error
        try:
            # Respond to tweet
            api.update_status(
                "Thank you @%s! Come again!" %
                tweet_author,
                in_reply_to_status_id=tweet_id)

            # Print success message
            print("Successful response!")

        except Exception:            # Print message if duplicate
            print("Already responded to this one!")

        # Print message to signify complete cycle
        print("We're done for now. I'll check again in 60 seconds.")
# Set timer to run every minute
while(True):
    ThankYou()
    time.sleep(60)