from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_safe


# Create your views here.

@require_safe
def start_game(request):
    return HttpResponse("Start game")


@require_safe
def index(request):
    return HttpResponse("Index page")
