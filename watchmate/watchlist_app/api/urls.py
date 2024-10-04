from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from watchlist_app.api.views import movie_list, movie_detail
# from watchlist_app.api.views import MovieListAPIView, MovieDetailAPIView 
from watchlist_app.api.views import (WatchListAV, WatchListDetailAV, StreamPlatformListAV, StreamPlatformDetailAV, ReviewListAV, 
                                     ReviewCreateAV,ReviewDetailAV, StreamPlatformViewSet) 

router = DefaultRouter()
router.register('stream',StreamPlatformViewSet, basename='streamplatform')

urlpatterns = [
    path('watchlist/', WatchListAV.as_view(), name= 'watch-list'),
    path('watchlist/<int:pk>/', WatchListDetailAV.as_view(), name = 'watch-list-detail'),
    
    # path('platform/', StreamPlatformListAV.as_view(), name= 'stream-platform-list'),
    # path('platform/<int:pk>/', StreamPlatformDetailAV.as_view(), name = 'stream-list-detail'),
    
    path('', include(router.urls)),
    
    
    # path('review/', ReviewListAV.as_view(), name= 'review-list'),
    # path('review/<int:pk>/', ReviewDetailAV.as_view(), name = 'review-detail'),
    
    path('watchlist/<int:pk>/review-create/', ReviewCreateAV.as_view(), name= 'review-create'),
    path('watchlist/<int:pk>/review/', ReviewListAV.as_view(), name= 'review-list'), # To get the reviews of a particualr watchlist
    path('watchlist/review/<int:pk>/', ReviewDetailAV.as_view(), name = 'review-detail'), # To access a particular review
    
    
    
    # path('list/', MovieListAPIView.as_view(), name= 'movie-list'),
    # path('list/<int:pk>/', MovieDetailAPIView.as_view(), name = 'movie-detail'),
    # path('list/', movie_list, name= 'movie-list'),
    # path('list/<int:pk>/', movie_detail, name = 'movie-detail'),
]