from django.shortcuts import render

from .helpers import get_places, post_places


def index(request):
    place = request.POST.get("place")

    if place:
        places_ids = get_places(place)

        for ids in places_ids:
            post_places(ids)

    return render(request, "index.html")
