from rest_framework import serializers

from core.models import Tweet

class TweetSerializer(serializers.ModelSerializer):
    """
    Serializer for the tweets
    """

    class Meta:
        model = Tweet
        fields = ('username','user_handle','user_imageURL','tweet_id','tweet_text','tweet_mediaURL','tweet_URL','post_date')