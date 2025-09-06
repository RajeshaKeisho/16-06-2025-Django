from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employeeView, name='employees'),
]