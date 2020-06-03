from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite = models.ManyToManyField('Recipe', symmetrical=False, related_name= 'favorites', default=None, blank = True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=40, default='')
    instructions = models.TextField(default="")
    

    def __str__(self):
        return self.title