from django.db import models


class Place(models.Model):
    place_id = models.CharField(max_length=42)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
