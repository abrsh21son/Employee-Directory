from django.shortcuts import get_object_or_404,render
from employees.models import employee

def employee_detail(request,id):
    employee_data=get_object_or_404(employee,id=id)
    context={
        "employee_data":employee_data
    }
    return render(request,'employee_detail.html',context)
