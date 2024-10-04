from django.urls import path, include
# from .views import movie_list, movie
from .views import WatchListAV, WatchListDetailAV, StreamPlatformListAV, StreamPlatformDetailAV
urlpatterns = [
    # path('list/', movie_list, name= 'movie-list'),
    # path('list/<int:pk>/', movie, name = 'movie'),
    
    path('watch_list/', WatchListAV.as_view(), name= 'watch-list'),
    path('watch_list/<int:pk>/', WatchListDetailAV.as_view(), name = 'watch-list-detail'),
    path('stream_platform_list/', StreamPlatformListAV.as_view(), name= 'stream-platform-list'),
    path('stream_platform_list/<int:pk>/', StreamPlatformDetailAV.as_view(), name = 'stream-list-detail'),
]