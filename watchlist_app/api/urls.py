from django.urls import path, include

import watchlist_app
from watchlist_app.api.views import StreamPlatform, WatchList, WatchDetailAV, StreamPlatformAV, WatchListAV, \
    StreamPlatformDetailAV, ReviewList, ReviewDetail
from watchlist_app.models import Review

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='movie-details'),
    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),

    path('review', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail')
]
