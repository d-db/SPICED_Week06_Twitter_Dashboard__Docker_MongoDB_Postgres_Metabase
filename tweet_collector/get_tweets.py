import tweepy
import os
import pymongo
import text2emotion as te

######################
# Connect to MongoDB #
######################

client = pymongo.MongoClient(host="mongodb", port=27017)
db_tweets = client.tweets

##################
# Authentication #
##################
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    wait_on_rate_limit=True,
)

########################
# Get User Information #
########################

# https://docs.tweepy.org/en/stable/client.html#tweepy.Client.get_user
# https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user

response_democrats = client.get_user(
    username='TheDemocrats',
    user_fields=['created_at', 'description', 'location',
                 'public_metrics', 'profile_image_url']
)

democrats = response_democrats.data


response_republicans = client.get_user(
    username='GOP',
    user_fields=['created_at', 'description', 'location',
                 'public_metrics', 'profile_image_url']
)

republicans = response_republicans.data



#######################
# Get a user's tweets #
#######################

# https://docs.tweepy.org/en/stable/pagination.html#tweepy.Paginator
# https://docs.tweepy.org/en/stable/client.html#tweepy.Client.get_users_tweets
# https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet

tweets_democrats = tweepy.Paginator(
    method=client.get_users_tweets,
    id=democrats.id,
    exclude=['replies', "retweets"],
    tweet_fields=["id", "created_at"],
    start_time="2022-01-01T00:00:00Z"
    # since_id=
).flatten()

democrat_count = 0

for tweet in tweets_democrats:
    tweet_dict = dict()
    tweet_dict["author"] = "Democrats"
    tweet_dict["text"] = dict(tweet)["text"]
    tweet_dict["id"] = dict(tweet)["id"]
    tweet_dict["created_at"] = tweet["created_at"]
    all_emotions_value = te.get_emotion(dict(tweet)["text"])
    tweet_dict["emotion"] = max(zip(all_emotions_value.values(), all_emotions_value.keys()))[1]
    db_tweets.tweets.insert_one(tweet_dict)
    democrat_count += 1

print(f"Democrats: {democrat_count}")

tweets_republicans= tweepy.Paginator(
    method=client.get_users_tweets,
    id=republicans.id,
    exclude=['replies', "retweets"],
    tweet_fields=["id", "created_at"],
    start_time="2022-01-01T00:00:00Z"
    # since_id=
).flatten()

republican_count = 0

for tweet in tweets_republicans:
    tweet_dict = dict()
    tweet_dict["author"] = "Republicans"
    tweet_dict["text"] = dict(tweet)["text"]
    tweet_dict["id"] = dict(tweet)["id"]
    tweet_dict["created_at"] = tweet["created_at"]
    all_emotions_value = te.get_emotion(dict(tweet)["text"])
    tweet_dict["emotion"] = max(zip(all_emotions_value.values(), all_emotions_value.keys()))[1]
    db_tweets.tweets.insert_one(tweet_dict)
    republican_count += 1

print(f"Republicans: {republican_count}")

#####################
# Search for Tweets #
#####################

# https://docs.tweepy.org/en/stable/client.html#tweepy.Client.search_recent_tweets
# https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query

# - means NOT
# search_query = "elon musk -is:retweet -is:reply -is:quote lang:de -has:links"
#
# cursor = tweepy.Paginator(
#     method=client.search_recent_tweets,
#     query=search_query,
#     tweet_fields=['author_id', 'created_at', 'public_metrics'],
# ).flatten(limit=20)
#
# for tweet in cursor:
#     print(tweet.text+'\n')
#     db.tweets.insert_one(dict(tweet))

