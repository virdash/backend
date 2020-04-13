from django.db import models

# Create your models here.
class Tweet(models.Model):
    """
    Tweet gotten from API
    """
    username = models.CharField(max_length=200)
    user_handle = models.CharField(unique=True, primary_key=True, max_length=200)
    user_imageURL = models.CharField(max_length=250, default='src/assets/images/profile.jpg')
    tweet_id = models.CharField(max_length=250, null=True, blank=True)
    tweet_text = models.TextField()
    tweet_mediaURL = models.URLField(max_length=250, blank=True)
    tweet_URL = models.URLField(max_length=250, default='https://twitter.com')
    post_date = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.tweet_text
