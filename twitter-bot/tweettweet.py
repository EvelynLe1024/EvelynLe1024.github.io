import tweepy
import time

auth = tweepy.OAuthHandler('cxFiY1djw50aPqGi4f1iNsU6Q', 'aCZzXCQEC8SoG1vkpdkYHFpO4Hqy0okbdmt9iOzq2ukv3Yo73n')
auth.set_access_token('1156588517687996421-934nRS9wqt39OY6Zc483UZqkLoCYcG', 'LUbP1Pd1MlFYdsanba69kQ7felCbs0H3n58ReyGVGeyzI')

api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)

search_string = 'python'
numberOfTweets = 2

#Narcissistic bot
for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)


# #Generous Bot
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     if follower.name == 'nocsdegree':
#         follower.follow()
#         break
