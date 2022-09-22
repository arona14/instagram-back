# import serializers from the REST framework
from rest_framework import serializers
from .models import Photo, Comment


class ImageSerializer(serializers.Serializer):
    image = serializers.ImageField()


class ProfileSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    bio = serializers.CharField(max_length=200)
    logo = serializers.ImageField()
    photos = ImageSerializer(many=True)
    num_photos = serializers.IntegerField()


class PhotoSerializer(serializers.ModelSerializer):
 
    # create a meta class
    class Meta:
        model = Photo
        fields = ('id', 'image', 'profile')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'profile', 'photo', 'content')


class PhotoRetrieveSerializer(serializers.ModelSerializer):
     
    comments = CommentSerializer(read_only=True, many=True)
    num_likes = serializers.IntegerField()
    class Meta:
        model = Photo
        fields = ('id', 'image', 'profile', 'comments', 'num_likes')
