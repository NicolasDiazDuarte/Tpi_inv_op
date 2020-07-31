<<<<<<< HEAD
from django.urls import path
from django.contrib import admin
from .views import index, RutaMasCorta


urlpatterns = [
    path('', index, name="index"),
    path('RMC/', RutaMasCorta),
