from rest_framework import generics, viewsets
from django.shortcuts import render
from .models import Artist, Album, Song
from .serializers import ArtistsSerializer, AlbumsSerializer, SongsSerializer
from drf_multiple_model.views import ObjectMultipleModelAPIView

# Create your views here.


class ArtistsList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistsSerializer

class AlbumsList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumsSerializer

class SongsList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongsSerializer

class MusicAPIView(ObjectMultipleModelAPIView):
    querylist  = [
        {'queryset': Artist.objects.all(), 'serializer_class': ArtistsSerializer},
        {'queryset': Album.objects.all(), 'serializer_class':AlbumsSerializer},
        {'queryset': Song.objects.all(), 'serializer_class':SongsSerializer},
    ]
    