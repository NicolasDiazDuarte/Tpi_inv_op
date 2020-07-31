from django.http import HttpResponse
from django.shortcuts import render

def index(request, *args, **kwargs):
    return render(request, "index.html", {})

def RutaMasCorta(request, *args, **kwargs):
    return render(request, "rutaMasCorta.html", {})
    