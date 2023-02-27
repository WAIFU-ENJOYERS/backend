from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def start_game(request):
    return HttpResponse("Start game")


def index(request):
    return HttpResponse("Index page")
