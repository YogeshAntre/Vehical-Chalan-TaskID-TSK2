# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    owner = models.CharField(max_length=20)
    registration_number = models.CharField(max_length=20, unique=True)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    year = models.IntegerField()

    def __str__(self):
        return self.registration_number

class Chalan(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"Chalan for {self.vehicle.registration_number} on {self.date}"
