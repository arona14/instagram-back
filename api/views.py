from django.shortcuts import render
 
# import view sets from the REST framework
from rest_framework import viewsets
from rest_framework.response import Response

 
# import the TodoSerializer from the serializer file
from .serializers import ProfileSerializer, PhotoSerializer, PhotoRetrieveSerializer, ProfileRetriveSerializer
from .models import Profile, Photo
 
# import the Todo model from the models file
from .models import Profile, Comment, Like
from .util.image import get_image_url
 
class ProfileView(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        queryset = Profile.objects.get(pk=pk)
        if queryset:
            queryset.username = queryset.user.username
            photos = Photo.objects.filter(profile=pk)
            photo_finals = []
            if photos:
                for photo in photos:
                    photo.image = get_image_url(photo.image)
                    photo_finals.append(photo)
            queryset.photos = photo_finals
            queryset.num_photos = len(photos)
            queryset.logo = get_image_url(queryset.logo)
            serializer = ProfileRetriveSerializer(queryset)
            return Response(serializer.data)


class PhotoView(viewsets.ModelViewSet):
     
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()

    def list(self, request):
        profile = request.query_params.get('profile')
        tag = request.query_params.get('tag')
        queryset = Photo.objects.all()
        qs = []
        for q in queryset:
            q.image = get_image_url(q.image)
            qs.append(q)
        if profile:
            queryset = qs.filter(profile__user__username=profile)
        if tag:
            qs = queryset.filter(tags__name__in=[tag])
        serializer = PhotoSerializer(qs, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        photo = Photo.objects.get(pk=pk)
        photo.image = get_image_url(photo.image)
        comments = Comment.objects.filter(photo=photo)
        photo.comments = comments
        num_likes = len(Like.objects.filter(photo=photo))
        photo.number_likes = num_likes
        serializer = PhotoRetrieveSerializer(photo)
        return Response(serializer.data)
