from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets

from watchlist_app.models import WatchList, StreamPlatform, Review
from watchlist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer

"""_
Viewsets and Router
"""

class StreamPlatformViewSet(viewsets.ViewSet):
    
    def list(self, request):
        queryset = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request,pk=None):
        queryset = StreamPlatform.objects.all()
        stream = get_object_or_404(queryset, pk=pk)
        serializer = StreamPlatformSerializer(stream)
        return Response(serializer.data)
    
    def create(self,request):
        serializer = StreamPlatformSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self,request,pk):
        stream = StreamPlatform.objects.get(pk=pk)
        stream.delete()
        return Response('Platform is deleted', status=status.HTTP_204_NO_CONTENT)
        

"""
 CreateAPIView
"""       
class ReviewCreateAV(generics.CreateAPIView):
    
    serializer_class = ReviewSerializer
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)
        
        # save the variable watchlist to the watchlist field
        serializer.save(watchlist=watchlist)
        
        
    

"""
Concrete View Classes - with custom queryset
"""

class ReviewListAV(generics.ListAPIView):
    
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        watchlist = self.kwargs['pk']
        return Review.objects.filter(watchlist=watchlist)

"""
Concrete View Classes - without custom queryset
"""

# class ReviewListAV(generics.ListCreateAPIView):
    
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

"""
Concrete View Classes  
"""
class ReviewDetailAV(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer 


"""
Generic class Views and Mixins  
"""

# class ReviewListAV(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     # ListModelMixin use get method
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     # CreateModelMixin used post method
#     def post(self,request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

"""
Generic class Views and Mixins  
"""

# class ReviewDetailAV(mixins.RetrieveModelMixin, generics.GenericAPIView):
    
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    

"""
ReviewListAV via API view
"""
# class ReviewListAV(APIView):
    
#     def get(self,request):
#         reviews = Review.objects.all()
#         serializer = ReviewSerializer(reviews, many=True)
        
#         return Response(serializer.data)
    
#     def post(self, request):
#         serializer = ReviewSerializer(data=request.data) 
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)



"""
ReviewDetailAV via API view
"""
# class ReviewDetailAV(APIView):
    
#     def get(self,request, pk):
#         try:
#             review = Review.objects.get(pk=pk)
#         except review.DoesNotExist:
#             return Response('The review does not exist', status=status.HTTP_404_NOT_FOUND)
#         serializer = ReviewSerializer(review)
        
#         return Response(serializer.data)
    
#     def put(self,request, pk):
#         review = Review.objects.get(pk=pk)
#         serializer = ReviewSerializer(review, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
#     def delete(self,request, pk):
#         review = Review.obejcts.get(pk=pk)
#         review.delete()
#         return Response("The review has been deleted", status=status.HTTP_204_NO_CONTENT)


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
            serializer.save()
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
        serializer = StreamPlatformSerializer(streams, many=True, context={'request': request}) # we need this for HyperLinkRelated Nested Serializer/HyperLinkModelSerializer
        # serializer = StreamPlatformSerializer(streams, many=True)
        
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
        try:
            stream = StreamPlatform.objects.get(pk=pk)
        except stream.DoesNotExist:
            return Response('Stream is not present', status=status.HTTP_404_NOT_FOUND)
        
        serializer = StreamPlatformSerializer(stream, context={'request': request})
        return Response(serializer.data)
    
    
    def put(self,request, pk):
        stream = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(stream, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    def delete(self, request, pk):
        stream = StreamPlatform.objects.get(pk=pk)
        stream.delete()
        return Response('Platform is deleted', status=status.HTTP_204_NO_CONTENT)



"""
MovieListAPIView via API view
"""
# class MovieListAPIView(APIView):
    
#     def get(self, request):
        
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
        
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
MovieDetailAPIView via API view
"""
# class MovieDetailAPIView(APIView):
    
#     def get(self, request, pk):
        
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error': 'Movie does not exist'}, status=status.HTTP_404_NOT_FOUND )
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
    
         
#     def put(self,request, pk):
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
#     def delete(self, request, pk):
        
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error': 'Movie does not exist'}, status=status.HTTP_404_NOT_FOUND )
#         name = movie
#         movie = movie.delete()
#         return Response({'message' : f'The movie {name} is deleted'}, status=status.HTTP_404_NOT_FOUND)
        
        

"""
Function Based Views
"""
# @api_view(['GET', 'POST'])
# def movie_list(request):
    
#     if request.method == 'GET':        
    
#         try:
#             movies = Movie.objects.all()
#         except Movie.DoesNotExist:
#             return Response({'error': 'The movie does not exist'}, status=status.HTTP_404_NOT_FOUND)
#             print(f'movies: {movies}')

#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request,pk):
    
#     if request.method == 'GET':
#         movie = Movie.objects.get(pk=pk)
#         print(f'Movie Name: {movie.name}')
#         print(f'Movie Description: {movie.description}')
#         print(f'Movie Active: {movie.active}')
#         serializer = MovieSerializer(movie)

#         return Response(serializer.data) 
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data) # Prepares the serializer for updating the movie instance
        
#         if serializer.is_valid():
#             serializer.save() # if the data is valid then will call update method of the MovieSerializer
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
        
#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         # print(f'movie_name: {movie}')
#         name = movie
#         movie.delete()
#         return Response({'message' : f'The movie {name} is deleted'}, status=status.HTTP_404_NOT_FOUND)
        
        