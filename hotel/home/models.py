from django.db import models
from datetime import date

# Create your models here.
class Dates(models.Model):
    arr_date = models.DateField(("Date"), default=date.today)
    dep_date = models.DateField(("Date"), default=date.today)

class City(models.Model):
    city = models.CharField(max_length=50)

class Hotels(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    cost = models.FloatField(default=0)
    hotel_name = models.CharField(max_length=100)
    def __str__(self):
        return self.hotel_name
