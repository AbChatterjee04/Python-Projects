import tweepy
import keys 

api_key = keys.api_key

api_secret = keys.api_secret

bearer_token = keys.bearer_token

access_token = keys.Access_token

access_token_secret = keys.Access_token_secret


# in order to establish connection
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)

api = tweepy.API(auth)


# how to tweet with command
# client.create_tweet(text = 'Hey there this is a test tweet with python commands #python')


# how to like a tweet
# client.like('1712581247770517872')  # all we need tweet id and basic plan free won't give u auth


# in order to retweet
# client.retweet('1712581247770517872') # all we need tweet id and basic plan free won't give u auth


# reply to tweet with command
# client.create_tweet(in_reply_to_tweet_id='1712581247770517872', text='reply test2')


# in order to extract all the tweets from timeline
for tweet in api.home_timeline():
    print(tweet.text)