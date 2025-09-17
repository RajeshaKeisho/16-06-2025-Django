from django.shortcuts import render, HttpResponse, redirect
from django.utils import timezone
from django.contrib import messages

# Create your views here.
USERS = {
    'admin':'password123',
    'user':'user123'
}


def home(request):
    username = request.session.get("username", "Guest")
    theme = request.COOKIES.get('theme', 'light')
    last_activity = request.session.get('last_activity', 'NO Activity Recorded')
    return render(request, 'home.html', {'username':username, 'theme':theme, 'last_activity':last_activity})



def set_cookie(request):
    response = HttpResponse("Cookie has been set")
    response.set_cookie('username', "Prasad", max_age=60)
    return response

def get_cookie(request):
    username = request.COOKIES.get('username', "GUEST")
    return HttpResponse(f"Hello, {username}!")


def set_session(request):
    request.session['user_id'] = 123
    request.session['last_activity'] = str(timezone.now())
    return HttpResponse("Session has been set!")


def get_session(request):
    user_id = request.session.get("user_id", "Not Logged In Yet")
    last_activity = request.session.get("last_activity", "No Activity Recorded")
    return HttpResponse(f"UserID: {user_id}, Last Activity: {last_activity}")

def clear_session(request):
    request.session.flush()
    return HttpResponse("Session has beed cleared!")


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username in USERS and USERS[username] == password:
            request.session['username'] = username
            request.session['last_activity']  = str(timezone.now())
            messages.success(request, "Login Successful!")
            return redirect("home")
        else:
            messages.error(request, "Invalid username or Password")
    return render(request, 'login.html')


def logout(request):
    request.session.flush()
    messages.success(request, 'You hav been successfully loggedout')
    return redirect('home')



def set_theme(request):
    if request.method == "POST":
        theme = request.POST.get('theme')
        response = redirect("home")
        response.set_cookie('theme', theme, max_age=30 * 24 * 60 * 60)

        messages.success(request, f'The theme has been set to {theme}.')
        return response
    return render(request, 'set_theme.html')


def protected_view(request):
    if 'username' not in request.session:
        messages.error(request, 'You mjust be logged in to access this page.')
        return redirect('login')
    return HttpResponse("This is a protected page. Only Logged in Users can visit.")