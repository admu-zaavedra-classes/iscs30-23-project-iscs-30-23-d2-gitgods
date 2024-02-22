from django.db import models

# Create your models here.

from django.utils import timezone

class Supplier(models.Model):
    name = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    created_at = models.DateTimeField(blank=True, null=True)

    def getName(self):
        return self.name
    
    def __str__(self):
        text = f'{self.name} - {self.city}, {self.country} created at: {self.created_at}'
        return text

class WaterBottle(models.Model):
    SKU = models.CharField(max_length=20)
    brand = models.CharField(max_length=300)
    cost = models.FloatField()
    size = models.CharField(max_length=50)
    mouth_size = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    supplied_by = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    current_quantity = models.IntegerField()

    def __str__(self):
        text = f'{self.SKU}: {self.brand}, {self.mouth_size}, {self.size}, {self.color}, supplied by {self.supplied_by.name}, {self.cost} : {self.current_quantity}'
        return text
    
class Account(models.Model):
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    objects = models.Manager()

    def getUsername(self):
        return self.username
    
    def getPassword(self):
        return self.password

    def __str__(self):
        return str(self.pk) + ": " + self.username + ", " + self.password