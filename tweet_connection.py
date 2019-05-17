from TwitterSearch import *
from models import model

class TweetConnection:

    def procurando_tweets(self, palavra_chave, idioma):
        tweets = []
        try:
            conexao = TwitterSearch(
                consumer_key = "kjJSuZiBHwNwY8BXg5ZFQRJ4y",
                consumer_secret = "zp4bzoEzPoTTq61nyfWJ6SV66kWBkXuiB3KzxUYWwdlsq8KK34",
                access_token = "1010185649448804353-ZaTEXJqt6w8jai16GtBjPgUUkhr7B0",
                access_token_secret = "sIF1uVph85e8IyBcFhkhPQadZ0aF0ET06TqfChHSZ7P69"
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




