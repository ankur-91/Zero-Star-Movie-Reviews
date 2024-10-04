from watchlist_app.models import WatchList, StreamPlatform, Review
from  rest_framework import serializers

"""
     serializers help in interacting with models by transforming model instances into JSON, XML, 
     or other content types (serialization) and vice versa (deserialization). 
     This allows your API to exchange data between your back-end and clients.
     It helps in creating custom fields, include validators and create relationships between models
"""
class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        # fields = '__all__'
        exclude = ('watchlist', )

class WatchListSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True, read_only=True) # Since we cannot add a review via WatchListSerializer, we can only read the reviews
    
    class Meta:
        model = WatchList
        fields = '__all__'
        # exclude = ['active']
    
    def get_len_name(self,object):
        length = len(object.title)
        return length
    
     # Object level validator
     # syntax: def validate() 
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError('Description and Name cannot be same')
    #     return data
        
    # # Field level validator
    # # syntax: def validate_fieldname
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError(f'The name of the movie {value} is too short')
    #     return value

# class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
class StreamPlatformSerializer(serializers.ModelSerializer):
    # len_name = serializers.SerializerMethodField()
    
    """
    Below fields are nested serializer
    """
    # watchlist name same as related_name in WatchList models field platform
    watchlist = WatchListSerializer(many=True, read_only=True) 
    # url = serializers.HyperlinkedIdentityField(view_name='streamplatform',lookup_field='pk')
    # url = serializers.HyperlinkedIdentityField(view_name='stream-list-detail',lookup_field='pk')
    # Will return the __str__ of the related field i.e from the WatchList model __str__
    # watchlist = serializers.StringRelatedField(many=True,read_only=True) 
    
    # Will also need to add context={'request': request} in the StreamPlatformListAV as well 
    # watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='watch-list-detail') 
    
    class Meta:
        model = StreamPlatform  
        fields = '__all__'
    
    # def get_len_name(self,object): # get_(same same as above field len_name)
    #     return len(object.name)


# def validate_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError('The name of the movie cannot be less than 2')
#     return value

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[validate_length]) # Validators
#     description = serializers.CharField()
#     active =  serializers.BooleanField()
    
#     def create(self, validated_data):
#         data = Movie.objects.create(**validated_data)
#         return data
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     # Object level validation
#     # syntax: def validate() 
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Description and Name cannot be same')
#         return data
        
#     # Field level validation
#     # syntax: def validate_fieldname
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError(f'The name of the movie {value} is too short')
#         return value
    