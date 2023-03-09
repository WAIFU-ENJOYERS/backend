from django.http import HttpResponse, HttpRequest
from django.views.decorators.http import require_safe
from pip._vendor.rich import json


# Create your views here.


@require_safe
def start_game(request: HttpRequest) -> HttpResponse:
    """Receive start game request."""
    return HttpResponse("Start game")


@require_safe
def index(request: HttpRequest) -> HttpResponse:
    """Sample index template request."""
    return HttpResponse("Index page")


@require_safe
def s3(request: HttpRequest) -> HttpResponse:
    """Sample demo request."""
    response_data = {
        "text": "Hello From Django",
        "gif": "https://thumbs.gfycat.com/AffectionateCheapFeline-max-1mb.gif",
    }
    return HttpResponse(json.dumps(response_data), content_type="application/json")
