from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path("",  views.home, name="home"),
    path("today/", views.get_today, name="today"),
    path("randpass/", views.get_random_pass, name="random_pass"),
    path("book/",  views.book , name="book"),
]