from django.db import models

# Create your models here.

class City(models.Model):
    cityID = models.CharField(max_length=3)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Hotel(models.Model):
    #city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    cityID = models.CharField(max_length=3)
    hotelID = models.CharField(max_length=5)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
    