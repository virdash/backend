from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tweets.views import get_tweet_view

app_name = 'tweets'

urlpatterns = [
  path('', get_tweet_view, name='tweets')
]
