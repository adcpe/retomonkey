from django.shortcuts import render

from .helpers import get_places, post_places


def index(request):
    place = request.POST.get("place")
    places = get_places(place)

    for place in places:
        post_places(place)

    return render(request, "index.html", {})
