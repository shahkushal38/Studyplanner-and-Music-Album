from django.db import models
from django.urls import reverse

# Create your models here.
class Album(models.Model):
    artist=models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField (max_length=100)
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('studyplanner:detail' , kwargs={"album_id": self.pk})
    
    def __str__(self):
        return self.album_title+ ' '+ self.artist
    

class Song(models.Model):
    album=models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type=models.CharField( max_length=100)
    song_title=models.CharField( max_length=250)
    is_favourite=models.BooleanField(default=False)

    def __str__(self):
        return self.song_title    

    

