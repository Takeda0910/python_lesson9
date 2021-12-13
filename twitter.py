import tweepy
import settings

consumer_key = settings.CK
consumer_secret = settings.CS
access_token = settings.AT
access_token_secret = settings.ATS


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def yes_stock_status():
    tweet = api.update_status("在庫有り")
    return tweet

def nothing_stock_status():
    tweet = api.update_status("在庫無し")
    return tweet

