from django.db import models


class Place(models.Model):
    place_id = models.CharField(max_length=42)
    name = models.CharField
    formatted_address = models.CharField
    formatted_phone_number = models.CharField
    rating = models.DecimalField(max_digits=2, decimal_places=1)
