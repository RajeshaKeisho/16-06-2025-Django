from django.contrib import admin
from .models import Employee, EmployeeProxy, Customer, CustomerProxy
# Register your models here.

admin.site.register(Employee)
admin.site.register(EmployeeProxy)
admin.site.register(Customer)
admin.site.register(CustomerProxy)
