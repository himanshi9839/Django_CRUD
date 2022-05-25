
from django.shortcuts import redirect, render
from crud2.models import Employees

# Create your views here.
def home(request):
    emp = Employees.objects.all()

    context = {
       'emp':emp, 
    }

    return render(request,'home.html',context)

def ADD(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees(
            name = name,
            email = email,
            address = address,
            phone = phone
        )

        emp.save()
        return redirect('home')

def EDIT(request):
    emp = Employees.objects.all()

    context = {
        'emp':emp
    }

    return redirect(request, 'home.html',context)

def UPDATE(request,id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employees(
            id = id,
            name = name,
            email = email,
            address = address,
            phone = phone
        )

        emp.save()
        return redirect('home')

    return redirect(request, 'home.html')

def DELETE(request,id):
    emp = Employees.objects.filter(id = id)
    emp.delete()
    
    context = {
        'emp':emp
    }
    
    return redirect('home')

    return render(request,'home.html')