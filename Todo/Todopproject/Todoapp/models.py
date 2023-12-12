from django.db import models


# Create your models here.
class Task(models.Model):
    Name=models.CharField(max_length=250)
    Priority=models.IntegerField()
    Date = models.DateField()

    def __str__(self):
        return self.Name
