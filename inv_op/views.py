from django.http import HttpResponse
from django.shortcuts import render


def index(request, *args, **kwargs):
    return render(request, "index.html", {})

def redes(request, *args, **kwargs):
    return render(request, "redes.html", {})

def RutaMasCorta(request, *args, **kwargs):
    return render(request, "rutaMasCorta.html", {})

def ExpansionMinima(request, *args, **kwargs):
    return render(request, "expansionMinima.html", {})