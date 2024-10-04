from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class StreamPlatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=200)
    
    def __str__(self) -> str:
       return self.name
    

class WatchList(models.Model):
  title = models.CharField(max_length = 150)
  storyline = models.TextField()
  active = models.BooleanField(default=True)
  platform = models.ForeignKey(StreamPlatform,on_delete=models.CASCADE, related_name='watchlist')
  created = models.DateTimeField(auto_now_add=True)
      
  def __str__(self):
      return self.title
  
class Review(models.Model):
  rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
  description = models.TextField()
  active = models.BooleanField(default=True)
  watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='reviews')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


  def __str__(self):
    return str(self.rating) + ' | ' + self.watchlist.title
