from django.db import models


class Place(models.Model):
    place_id = models.TextField()
    name = models.TextField()
    address = models.TextField()
    maps_url = models.TextField()


"""
Model       |   Google Maps API
------------|---------------------
place_id    |   place_id
name        |   name
address     |   formatted_address
maps_url    |   url
"""
