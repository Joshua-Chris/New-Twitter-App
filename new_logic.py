import os
import tweepy as tw
import pandas as pd
import geocoder

import twitter_credentials

auth = tw.OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_secret)
auth.set_access_token(twitter_credentials.access_token, twitter_credentials.access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

# useful variables
search_query = "corona place:%s"
date_since = "2020-01-11"

places = api.geo_search(query="Nigeria", granularity="country")
place_id = places[0].id

# collect tweets
tweets = tw.Cursor(api.search,
              q=search_query % place_id,
              lang="en",
              since=date_since).items(100)

for tweet in tweets:

    print(tweet.text + " | >>>>>>>>>>>>>>>> " + tweet.place.name if tweet.place else "Undefined place")
    print("Number of Retweets:")
    print(tweet.retweet_count)
    print("Number of likes:")
    print(tweet.favorite_count)
    print("-------------------------------------")


