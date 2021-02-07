from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from music import views

urlpatterns = [
    path('artists/api', views.ArtistsList.as_view()),
    path('albums/api', views.AlbumsList.as_view()),
    path('songs/api', views.SongsList.as_view()),
    path('music/api', views.MusicAPIView.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)