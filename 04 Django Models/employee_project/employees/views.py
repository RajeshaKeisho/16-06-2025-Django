from django.shortcuts import render
from .models import Employee
# Create your views here.
def employeeView(request):
    employees = Employee.objects.all()

    my_dict = {'emp_data':employees}

    return render(request, 'employees.html', context=my_dict)