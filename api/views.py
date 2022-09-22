from django.shortcuts import render
 
# import view sets from the REST framework
from rest_framework import viewsets
from rest_framework.response import Response

 
# import the TodoSerializer from the serializer file
from .serializers import ProfileSerializer, PhotoSerializer, PhotoRetrieveSerializer
from .models import Profile, Photo
 
# import the Todo model from the models file
from .models import Profile, Comment, Like
 
class ProfileView(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Profile.objects.get(pk=pk)
        if queryset:
            queryset.username = queryset.user.username
            photos = Photo.objects.filter(profile=pk)
            queryset.photos = photos
            queryset.num_photos = len(photos)
            serializer = ProfileSerializer(queryset)
            return Response(serializer.data)


class PhotoView(viewsets.ModelViewSet):
     
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()

    def list(self, request):
        profile_id = request.query_params.get('profile')
        queryset = Photo.objects.all()
        if profile_id:
            queryset = queryset.filter(profile=profile_id)
        serializer = PhotoSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        photo = Photo.objects.get(pk=pk)
        comments = Comment.objects.filter(photo=photo)
        photo.comments = comments
        num_likes = len(Like.objects.filter(photo=photo))
        photo.num_likes = num_likes
        serializer = PhotoRetrieveSerializer(photo)
        return Response(serializer.data)
