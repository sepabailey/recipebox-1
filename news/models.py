from django.db import models
from django.utils import timezone

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class NewsItem(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=40, default='')
    instructions = models.TextField(default="")

    def __str__(self):
        return self.title