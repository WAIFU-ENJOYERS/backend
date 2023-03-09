from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("start-game", views.start_game),
    path("s3", views.s3),
]
