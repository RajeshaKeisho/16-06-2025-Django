from django.http import HttpResponse
# Create your views here.
import datetime
from django.utils import timezone


def display(request):
    s = "<h1>Hello, Students! Welcome to Django Class!</h1>"
    return HttpResponse(s)

def my_view(request):
    return HttpResponse("Hello, Python World!")


def greeting(request):
    current_time = timezone.now()
    hour = current_time.hour


    if 6 <= hour < 12:
        greeting_message = "Good Morning"
    elif 12 <= hour <= 16:
        greeting_message = "Good Noon"

    elif 16 <= hour <= 21:
        greeting_message = "Good Evening"

    else:
        greeting_message = "Good Night"

    formatted_time = current_time.strftime("%d-%m-%Y %H:%M:%S")
    return HttpResponse(f"{greeting_message}. Today, the date and time is {formatted_time}!")
