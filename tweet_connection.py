from TwitterSearch import *
from models import model

class TweetConnection:

    def procurando_tweets(self, palavra_chave, idioma):
        tweets = []
        try:
            conexao = TwitterSearch(
                consumer_key = "***",
                consumer_secret = "***",
                access_token = "***",
                access_token_secret = "***"
            )

            cursor = TwitterSearchOrder()
            print("key:", palavra_chave)
            cursor.set_keywords([palavra_chave])
            cursor.set_language(idioma)

            for tweet_achado in conexao.search_tweets_iterable(cursor):
                tw = model.Tweet(tweet_achado["user"]["screen_name"], tweet_achado["text"])
                tweets.append(tw)

        except TwitterSearchException as e:
            print(e)

        return tweets




