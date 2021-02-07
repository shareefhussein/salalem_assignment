from rest_framework import serializers
from .models import Artist, Album, Song

class ArtistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class AlbumsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
