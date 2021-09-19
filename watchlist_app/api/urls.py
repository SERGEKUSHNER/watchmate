from django.urls import path, include

import watchlist_app
from watchlist_app.api.views import StreamPlatform, WatchList, WatchDetailAV, StreamPlatformAV, WatchListAV, \
    StreamPlatformDetailAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='movie-details'),
    path('stream/', StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='streamplatform-detail')
]
