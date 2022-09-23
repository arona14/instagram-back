# import serializers from the REST framework
from rest_framework import serializers
from taggit.serializers import (TagListSerializerField,
                            TaggitSerializer)
from django.contrib.auth.models import User
from .models import Photo, Comment, Profile


class ImageSerializer(serializers.Serializer):
    image = serializers.CharField()


class ProfileRetriveSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField(max_length=200)
    bio = serializers.CharField(max_length=200)
    logo = serializers.CharField()
    photos = ImageSerializer(many=True)
    num_photos = serializers.IntegerField()


class UserSerializer(serializers.ModelSerializer):
    
     class Meta:
            model = User
            fields = ('username', )
class ProfileSerializer(serializers.ModelSerializer):
    
    user = UserSerializer(read_only=True)
    class Meta:
            model = Profile
            fields = ('id', 'bio', 'user')


class PhotoSerializer(TaggitSerializer, serializers.ModelSerializer):
    
    tags = TagListSerializerField()
    profile = ProfileSerializer(read_only=True)
    image = serializers.CharField()
    class Meta:
        model = Photo
        fields = ('id', 'image', 'profile', 'tags')


class CommentSerializer(serializers.ModelSerializer):

    profile = ProfileSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'profile', 'content')


class PhotoRetrieveSerializer(serializers.ModelSerializer):
     
    comments = CommentSerializer(read_only=True, many=True)
    number_likes = serializers.IntegerField()
    profile = ProfileSerializer(read_only=True)
    image = serializers.CharField()
    tags = TagListSerializerField()
    class Meta:
        model = Photo
        fields = ('id', 'image', 'profile', 'comments', 'number_likes', 'tags')
