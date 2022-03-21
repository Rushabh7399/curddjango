from django.shortcuts import render, redirect, HttpResponse
from .models import Employee5
from django.contrib import messages
# Create your views here.
def createView(request):
    return render(request, 'create.html')


def store(request):
    emp = Employee5()
    emp.emp_name = request.POST.get('emp_name')
    emp.emp_email = request.POST.get('emp_email')
    emp.emp_number = request.POST.get('emp_mobile')
    res = ""
    objects = Employee5.objects.all()
    for objec in objects:
        if objec.emp_name == emp.emp_name:
            messages.error(request, f"Employee already exist")
            return redirect('/employee/create')

    emp.save()
    messages.success(request, f"Employee Added Successfully {res} result")
    return redirect('/employee/create')

def show_emp(request):
    all_emp = Employee5.objects.all()
    return render(request, 'index.html', {"emp": all_emp})

def delete_emp(request, emp_id):
    print("HELLO")
    emp_id = Employee5.objects.get(id=emp_id)
    print(emp_id)
    emp_id.delete()
    messages.success(request, "Employee deleted successfully")
    return redirect('/employee/create')

def update_view(request, emp_id):
    emp = Employee5.objects.get(id=emp_id)
    return render(request, 'update.html', {"employee": emp})

def edit(request, emp_id):
    emp = Employee5.objects.get(id=emp_id)
    emp.emp_name = request.POST.get("emp_name")
    emp.emp_email = request.POST.get("emp_email")
    emp.emp_number = request.POST.get("emp_mobile")
    emp.save()
    messages.success(request, "Employee detail updated successfully")
    return redirect("employee/")

def view(request, emp_id):
    emp = Employee5.objects.get(id=emp_id)
    return render(request, 'emp_view.html', {"employee": emp})

def test_view(request):
    return HttpResponse("<p>HELLO WORLD</p>")

