from django.db import models

# Create your models here.
class cars(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
       return self.name


class client(models.Model):
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    name = models.CharField(max_length=250)
    place= models.CharField(max_length=100)

    def __str__(self):
        return self.name