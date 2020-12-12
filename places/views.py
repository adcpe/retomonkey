from django.shortcuts import HttpResponse


def index(request):
    return HttpResponse("Esta es una vista")
