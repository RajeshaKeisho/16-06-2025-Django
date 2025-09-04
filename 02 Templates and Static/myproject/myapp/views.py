from django.shortcuts import render
import datetime
# Create your views here.

def wish(request):
    time = datetime.datetime.now()
    name = "Prasad"
    age = 25
    marks = 90
    formatted_time = time.strftime("%d-%m-%Y %H:%M:%S")
    my_dict = {'insert_time':formatted_time, 'name':name, 'age':age, 'marks':marks}
    return render(render, 'wish.html', my_dict)


def greet(request):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if now.hour < 12:
        greeting = "Good Morning"
    elif now.hour < 16:
        greeting = "Good Noon"
    elif now.hour < 21:
        greeting = "Good Evening"
    else:
        greeting = "Good Night"
    return render(request, 'myapp/greet.html', {'greeting':greeting, "time":current_time })

