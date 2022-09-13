from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from datetime import date
import random
import string

# Create your views here.


def home(request : HttpRequest):
    msg_str = "Welcom to this website !"
    return render(request, 'home/index.html', {"msg" : msg_str})


def get_today(request : HttpRequest):
    today = date.today()

    return render(request, 'home/today.html', {"today" : today})

def get_random_pass(request : HttpRequest):
    random_password = "".join(random.choices(string.ascii_letters + string.digits, k=9))
    
    return render(request, "home/randpass.html", {"randpass" : random_password})

def book(request : HttpRequest):
    book = ["introduction to CS ", "FinTech", "Python for bigner "]
    return render(request, 'home/book.html', { "book" : book})