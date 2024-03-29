import os
import environ
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import tweepy
import random

from core.models import Tweet
from tweets.serializers import TweetSerializer


env = environ.Env()

# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Take environment variables from .env file
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# False if not in os.environ because of casting above
consumer_key = env('CUSTOMER_KEY')
consumer_secret = env('CUSTOMER_SECRET')
access_token = env('ACCESS_TOKEN')
access_token_secret = env('ACCESS_TOKEN_SECRET')



def get_tweet():
  """
  Manage tweets in the database
  """
  # Authenticate tweepy
  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_token, access_token_secret)

  # creation of the actual interface, using authentication
  api = tweepy.API(auth, wait_on_rate_limit=True)

  sources = ["WHO","NCDCgov","Ecowas_cdc"]
  tweets_list = []

  # Get tweets
  for source in sources:
    tweets = tweepy.Cursor(api.user_timeline,screen_name=source, include_entities=True).items(20)

    for item in tweets:
      img_url = ""

      if 'media' in item.entities:
        for image in item.entities['media']:
          img_url = image['media_url']

      tweets_list.append(
        {
          "username": item.user.name,
          "user_handle": item.user.screen_name,
          "user_imageURL": item.user.profile_image_url_https,
          "tweet_id": item.id,
          "tweet_text":item.text,
          "tweet_mediaURL": img_url,
          "tweet_URL": "https://twitter.com/" + item.user.screen_name + "/status/" + str(item.id),
          "post_date": item.created_at,
        }
      )

  return tweets_list

@api_view(['GET',])
def get_tweet_view(request):
  try:
    tweets_list = get_tweet()
    
    # Shuffle tweets
    random.shuffle(tweets_list)
 
  except Tweet.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == "GET":
    serializers = TweetSerializer(tweets_list, many=True)
    return Response(serializers.data)
