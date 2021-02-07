from django.db import models

# Create your models here.
class Artist(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='img', blank=True)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name  


class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    song_genre =  models.CharField(max_length=10)
    song_title= models.CharField(max_length=100 ,default='')
    image = models.ImageField(upload_to='img', blank=True)
    
    def __str__(self):
            return self.song_title +'-'+ self.artist.first_name +' '+ self.artist.last_name


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True )
    album_title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    songs = models.ManyToManyField(Song)
    image = models.ImageField(upload_to='img', blank=True)


    def __str__(self):
        return self.album_title +'-'+ self.artist.first_name +' '+ self.artist.last_name            