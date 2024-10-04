from django.shortcuts import render
from .models import WatchList, StreamPlatform
from django.http import JsonResponse
from django.core.serializers import serialize
from rest_framework import status,APIView
from .api.serializers import WatchListSerializer, StreamPlatformSerializer
from rest_framework.response import Response
import json

# def movie_list(request):
    
#     movies = Movie.objects.all()
#     movie_list = list(movies.values())#     data = {'movies': movie_list}
    
#     return JsonResponse(data)

# def movie(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     print(f'type of movie: {type(movie)}')
#     movie_data = serialize('json', [movie])
#     print(f'movie_data1: type = {type(movie_data)}, data = {movie_data}')
#     # movie_data = movie_data[1:-1]
#     movie_data = json.loads(movie_data)[0]
#     print(f'movie_data2: type = {type(movie_data)}, data = {movie_data}')
#     # data = {'movie': list(movie)}
    
#     return JsonResponse(movie_data)

"""
    Don't consider this view. refer watchlist_app.api.views
"""
class WatchListAV(APIView):
# class MovieListAV(APIView):
    
    def get(self, request):
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)
        
        return Response(serializer.data)
    
    def post(self, request):
        serailizer = WatchListSerializer(data=request.data)
        if serailizer.is_valid():
            serailizer.save()
            return Response(serailizer.data)
        else:
            return Response(serailizer.errors)
        
class WatchListDetailAV(APIView):  
# class MovieDetailAV(APIView):
    
    def get(self, request,pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except movie.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)
    
    
    def put(self,request,pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self,request,pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
class StreamPlatformListAV(APIView):
    
    def get(self, request):
        streams = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(streams, many=True)
        
        return Response(serializer.data)
    
    def post(self,request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class StreamPlatformDetailAV(APIView):
    
    def get(self,request,pk):
        stream = StreamPlatform.objects.get(pk=pk)
        if stream.DoesNotExist:
            return Response('Stream is not present', status=status.HTTP_404_NOT_FOUND)
        
        serializer = StreamPlatformSerializer(stream)
        return Response(serializer.data)
    
    
    def put(self,request, pk):
        stream = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(stream, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self, request, pk):
        stream = StreamPlatform.objects.get(pk=pk)
        stream.delete()
        return Response('Objects is deleted', status=status.HTTP_204_NO_CONTENT)
    
    
    
           
            