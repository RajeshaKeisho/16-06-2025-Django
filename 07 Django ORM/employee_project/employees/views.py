from django.shortcuts import render
from django.db.models import Avg, Count, Q
from .models import Employee, Department
from django.db import connection


def all_employees(request):
    employees = Employee.objects.all()
    return render(request, 'employees/all_employees.html', {'employees':employees})

def it_department_employees(request):
    it_employees = Employee.objects.filter(department__name='IT')
    return render(request, 'employees/it_department_employees.html', {'it_employees': it_employees})

def high_salary_employees(request):
    high_salary_employees = Employee.objects.filter(salary__gt=55000)
    return render(request, 'employees/high_salary_employees.html', {'high_salary_employees': high_salary_employees})

def avg_salary(request):
    avg_salary = Employee.objects.aggregate(avg_salary=Avg('salary'))
    return render(request, 'employees/avg_salary.html', {'avg_salary': avg_salary})

def high_paid_employees(request):
    
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM employees_employee WHERE salary > 60000")
        employees = cursor.fetchall()

 
    employee_objects = [Employee(*row) for row in employees]

    return render(request, 'employees/employee_list.html', {'employees': employee_objects})

