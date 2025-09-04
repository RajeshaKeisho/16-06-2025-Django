from django.urls import path
from . import views
urlpatterns = [
    path('display/', views.display, name='display'),
    path('my_view/', views.my_view, name='my_view'),
    path('greeting/', views.greeting, name='greetingw'),
]