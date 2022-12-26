import time
import pymongo
import re
from sqlalchemy import create_engine
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# import emoji
# import contractions

time.sleep(480)  # seconds

# Connect to postgres and create a table to store the tweets
engine = create_engine('postgresql://postgres:postgres@postgresdb:5432/twitter_db', echo=True)

engine.execute('''
    CREATE TABLE IF NOT EXISTS tweets (
    author VARCHAR(500),
    text VARCHAR(500),
    sentiment_po DECIMAL,
    sentiment_neu DECIMAL,
    sentiment_neg DECIMAL,
    sentiment_com DECIMAL,
    emotion VARCHAR(500),
    best_category  TEXT,
    id  NUMERIC,
    created_at TIMESTAMP
);
    ''')

# Connect to MongoDB
client = pymongo.MongoClient(host="mongodb", port=27017)
db_tweets = client.tweets

# Select the database you want to use withing MongoDB
# db_democrats = client.democrats
# db_republicans = client.republicans
#
# db_list = [db_democrats, db_republicans]


def extract():
    extracted_tweets = db_tweets.tweets.find()
    return extracted_tweets


def transform(extracted_tweets):
    transformed_tweets = []
    for tweet in extracted_tweets:
        text = tweet['text']

        # Removing links
        regex = "https:\/\/t.co\/[\w]{10}"
        text = re.sub(regex, "", text)

        # Removing the newline charakter from
        text = text.replace("\n", "")

        # Calculate Sentiment scores
        pos, neu, neg, com, best_cat = sentiment_scores(text)

        transformed_tweets.append([tweet["author"], text, pos, neu, neg, com,
                                   tweet["emotion"], best_cat, tweet["id"], tweet["created_at"]])
    return transformed_tweets


def sentiment_scores(sentence):
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()

    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)
    best_category = rather_pos_or_neg(sentiment_dict['pos'], sentiment_dict['neg'])

    return sentiment_dict['pos'], sentiment_dict['neu'], sentiment_dict['neg'], sentiment_dict['compound'], best_category


def rather_pos_or_neg(score_pos, score_neg):
    list_scores = [score_pos, score_neg]
    max_val = max(list_scores)
    idx_max = list_scores.index(max_val)

    if idx_max == 0:
        return "Positiv"
    else:
        return "Negativ"


def load(transformed_tweets):
    print(f"Length of 'transformed tweets' {len(transformed_tweets)}")
    for tweet in transformed_tweets:
        insert_query = f"INSERT INTO tweets VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING"
        engine.execute(insert_query, (tweet[0], tweet[1], tweet[2], tweet[3], tweet[4],
                                      tweet[5], tweet[6], tweet[7], tweet[8], tweet[9]))


if __name__ == '__main__':
    extracted_tweets = extract()
    transformed_tweets = transform(extracted_tweets)
    load(transformed_tweets)
    # time.sleep(600)