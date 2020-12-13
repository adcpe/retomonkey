import requests
import environ

from .models import Place

env = environ.Env()
environ.Env.read_env()

API_KEY = env("API_KEY")


def get_places(search):
    url = f"https://maps.googleapis.com/maps/api/place/autocomplete/json?key={API_KEY}&input={search}"
    r = requests.get(url).json()["predictions"]
    ids = [place["place_id"] for place in r]
    return ids


def post_places(place_id):
    url = f"https://maps.googleapis.com/maps/api/place/details/json?key={API_KEY}&place_id={place_id}"
    r = requests.get(url).json()["result"]

    p = Place()
    p.place_id = place_id
    p.name = r["name"]
    p.address = r["formatted_address"]
    p.maps_url = r["url"]
    p.save()
