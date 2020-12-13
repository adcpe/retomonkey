from django.db import models


class Place(models.Model):
    place_id = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    maps_url = models.CharField(max_length=200)


"""
Model       |   Google Maps API
------------|---------------------
place_id    |   place_id
name        |   name
address     |   formatted_address
maps_url    |   url
"""
