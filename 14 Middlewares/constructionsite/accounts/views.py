from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse("<html><body><h1>About Page</h1><p>This is about page.</p></body></html>")

def sample_view(request):
    if 'error' in request.GET:
        raise ValueError("An intentional error occurred!")
    return HttpResponse("This is a sample view without errors.")