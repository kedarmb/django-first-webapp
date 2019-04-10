from django.shortcuts import render,redirect
from crud.forms import EmployeeForm
from crud.models import Employee
from django.contrib.auth.decorators import login_required

# Create your views here.
# def crud(request):
#     return render(request,'crud.html')


def create(request):
    form = EmployeeForm()

    if request.method == 'POST':
        print(request.method)
        form = EmployeeForm(request.POST)
        if form.is_valid():
            # pass
            formData = form.cleaned_data
            emp = Employee()
            emp.emp_name = formData['emp_name']
            emp.emp_email = formData['emp_email']
            emp.emp_address = formData['emp_address']
            emp.save()
            return redirect(index)


    print(form)
    data = {
        "form" : form
    }
    return render(request,'create.html',data)
@login_required(login_url='/signin')
def index(request):
    # select * from employee
    data = Employee.objects.all()
    # data = Employee.objects.raw("select * from employee")
    return render(request,'index.html', {"data":data})

def update(request):
    print(request.GET['id'])
    id = request.GET['id']
    data = Employee.objects.get(id=id)
    # form = EmployeeForm()
    form = EmployeeForm(instance=data)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=data)
        if form.is_valid():
            formData = form.cleaned_data
            emp = Employee()
            emp.id = id #update
            emp.emp_name = formData['emp_name']
            emp.emp_email = formData['emp_email']
            emp.emp_address = formData['emp_address']
            emp.save()
            return redirect(index)
    d1 = {"form" : form}
    return render(request,'update.html',d1)

def delete(request):
    id = request.GET['id']
    data = Employee.objects.get(id=id)
    data.delete()

    return redirect(index)

def view(request):
    id = request.GET['id']
    data = Employee.objects.get(id=id)
    return render(request,'view.html',{"data":data})