from django.urls import path, include
from rest_framework.routers import DefaultRouter

import watchlist_app
from watchlist_app.api.views import (  WatchDetailAV,  WatchListAV,
                                      ReviewList, ReviewDetail, ReviewCreate, StreamPlatformVS)
from watchlist_app.models import Review

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')


urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>', WatchDetailAV.as_view(), name='movie-details'),

    path('', include(router.urls)),

    # path('stream/', StreamPlatformAV.as_view(), name='stream'),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='streamplatform-detail'),

    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail')

    path('stream/<int:pk>/review-create', ReviewCreate.as_view(), name='review-list'),
    path('stream/<int:pk>/review', ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),

]
