import tweepy
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

APIKEY = os.getenv("APIKEY")
APIKEYSECRET = os.getenv("APIKEYSECRET")
BEARERTOKEN = os.getenv("BEARERTOKEN")
ACCESSTOKEN = os.getenv("ACCESSTOKEN")
ACCESSTOKENSECRET = os.getenv("ACCESSTOKENSECRET")

auth = tweepy.OAuthHandler(APIKEY, APIKEYSECRET)
auth.set_access_token(ACCESSTOKEN, ACCESSTOKENSECRET)

api = tweepy.API(auth)


class Twitter:

    def get_id(self, link):
        temp = link.split("/")[-1]
        id = temp.split('?')[0]
        return id

    def get_name(self, tweet):
        name = tweet.author._json['name']
        screen = tweet.author._json['screen_name']
        return (name, screen)

    def get_hashtags(self, tweet):
        hashtags = [hashtag["text"] for hashtag in tweet.entities["hashtags"]]
        return hashtags

    def get_mentions(self, tweet):
        entities = tweet._json["entities"]
        screen = [mention["screen_name"]
                  for mention in tweet._json["entities"]["user_mentions"]]
        name = [mention["name"]
                for mention in tweet._json["entities"]["user_mentions"]]
        return (screen, name)

    def get_text(self, tweet):
        try:
            return tweet.full_text
        except:
            return tweet.text

    def get_favorites(self, tweet):
        return tweet.favorite_count

    def get_retweets(self, tweet):
        return tweet.retweet_count

    def get_media(self, tweet):
        if "extended_entities" not in tweet._json:
            return []
        urls = [media['media_url']
                for media in tweet._json['extended_entities']['media']]
        return urls

    def get_data(self, link):
        id = self.get_id(link)
        t = api.get_status(id, tweet_mode="extended")
        name, mentions, text, favorites, retweets, media, hashtags = self.get_name(t), self.get_mentions(t), self.get_text(
            t), self.get_favorites(t), self.get_retweets(t), self.get_media(t), self.get_hashtags(t)
        return name, mentions, text, favorites, retweets, media, hashtags
