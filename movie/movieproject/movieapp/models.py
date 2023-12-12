from django.db import models


# Create your models here.
class Movie(models.Model):
    Name=models.CharField(max_length=250)
    desc=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='downloads')

    def __str__(self):
        return self.Name