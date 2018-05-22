from django.db import models

# Create your models here.

class City(models.Model):
	ID = models.CharField(max_length=3, primary_key=True)
	name = models.CharField(max_length=20, unique=True)

	def __str__(self):
		return self.name

class Hotel(models.Model):
	#city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
	cityID = models.CharField(max_length=3)
	ID = models.CharField(max_length=5, primary_key=True)
	name = models.CharField(max_length=40)
	