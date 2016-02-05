# encoding: utf-8
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bonjour. Bienveu à l'index des propositions de jeu.")

# Create your views here.
