from django.contrib import admin
from . models import cars
from .models import client
# Register your models here.
admin.site.register(cars)
admin.site.register(client)