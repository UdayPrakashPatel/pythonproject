from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from multiprocessing import context
from django.shortcuts import redirect, render
from .forms import EmployeeForm
from .models import Employee
# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')
def WebHomePage(request):
    return render (request,'webHomePage.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')



# Create your views here crud opretion.
def Home(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        form.save()
        form=EmployeeForm()
    
    data=Employee.objects.all()  


    context={
        'form':form,
        'data':data,
    }
    return render(request,'index.html',context)

# Delete View
def Delete_record(request,id):
    a=Employee.objects.get(pk=id)
    a.delete()
    return redirect('index')
    

# Update View
def Update_Record(request,id):
    if request.method=='POST':
        data=Employee.objects.get(pk=id)
        form=EmployeeForm(request.POST,instance=data)
        if form.is_valid():
            form.save()           
    else:

        data=Employee.objects.get(pk=id)
        form=EmployeeForm(instance=data)
    context={
        'form':form,
    }
    return render (request,'update.html',context)

