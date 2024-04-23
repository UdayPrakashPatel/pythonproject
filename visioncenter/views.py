from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from multiprocessing import context
from django.shortcuts import redirect, render
from .forms import EmployeeForm
from .models import Employee
from django.contrib import messages
from .models import CustomUser
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CustomUser  # Assuming your CustomUser model is defined in models.py
from django.http import HttpResponse
import re

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')
def WebHomePage(request):
    return render (request,'webHomePage.html')

# def SignupPage(request):
#      if request.method=='POST':
#          uname=request.POST.get('username')
#          email=request.POST.get('email')
#          pass1=request.POST.get('password1')
#          pass2=request.POST.get('password2')
#          direction = request.POST.get('direction')

#          if pass1!=pass2:
#              return HttpResponse("Your password and confrom password are not Same!!")
#          else:

#              my_user=User.objects.create_user(uname,email,pass1)
#              my_user.save()
#              return redirect('login')    
#      return render (request,'signup.html')

def SignupPage(request):
    error_message = None
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        direction = request.POST.get('direction')

        if User.objects.filter(username=uname).exists():
            error_message = "Username is already taken. Please choose a different one."
        elif pass1 != pass2:
            error_message = "Your password and confirm password are not the same!"
        elif not re.match(r'^\w+[\w\.-]*@gmail\.com$', email):
            error_message = "Please input a correct email address."
        else:
            mixed_input = ' '.join([word.capitalize() if idx == 0 else word.lower() for idx, word in enumerate(re.findall(r'\w+', direction))])
            mixed_input += '@'
            mixed_input += ''.join(re.findall(r'\d', pass1))
            mixed_input += '_'.join(re.findall(r'[a-z]{2}', pass1))

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html', {'error_message': error_message})





# def SignupPage(request):
#     if request.method == 'POST':
#         uname = request.POST.get('username')
#         email = request.POST.get('email')
#         pass1 = request.POST.get('password1')
#         pass2 = request.POST.get('password2')
#         direction = request.POST.get('direction')

#         if pass1 != pass2:
#             return HttpResponse("Your password and confirm password do not match!")
#         else:
#             # Create the user object without setting the direction initially
#             my_user = User.objects.create_user(username=uname, email=email, password=pass1)
            
#             # Get or create the associated CustomUser instance
#             custom_user, created = CustomUser.objects.get_or_create(user=my_user)
#             custom_user.direction = direction
#             custom_user.save()

#             return redirect('login')

#     return render(request, 'signup.html')


from django.contrib.auth import authenticate, login

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or Password is incorrect!!!")
            return redirect('login')

    return render(request, 'login.html')
  

# def LoginPage(request):
#     if request.method=='POST':
#         username=request.POST.get('username')
#         pass1=request.POST.get('pass')
#         user=authenticate(request,username=username,password=pass1)
#         if user is not None:
#             login(request,user)
#             return redirect('home')
#         else:
#             messages.error(request, "Username or Password is incorrect!!!")
#             return redirect('login')
#             #return HttpResponse ("Username or Password is incorrect!!!")

#     return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

# def ForgetPassword(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password1 = request.POST.get('password1')
#         password2 = request.POST.get('password2')
#         direction = request.POST.get('direction')

#         try:
#             # Check if the user with the provided username exists
#             user = CustomUser.objects.get(username=username)
#         except CustomUser.DoesNotExist:
#             # If the user does not exist, show an error message
#             messages.error(request, "This username does not exist.")
#             return redirect('forget_password')

#         if password1 != password2:
#             # If passwords do not match, show an error message
#             messages.error(request, "Passwords do not match.")
#             return redirect('forget_password')

#         # Set the new password for the user
#         user.set_password(password1)
#         user.direction = direction  # Save the direction value to the user object
#         user.save()

#         # You can perform additional actions here if needed, such as sending a confirmation email to the user

#         messages.success(request, "Your password has been successfully changed.")
#         return redirect('login')

#     return render(request, 'ForgetPassword.html')

def ForgetPassword(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        direction = request.POST.get('direction')

        try:
            # Check if the user with the provided username exists
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # If the user does not exist, show an error message
            messages.error(request, "This username does not exist.")
            return redirect('forget_password')

        if password1 != password2:
            # If passwords do not match, show an error message
            messages.error(request, "Passwords do not match.")
            return redirect('forget_password')

        # Set the new password for the user
        user.set_password(password1)
        user.save()

        # You can perform additional actions here if needed, such as sending a confirmation email to the user

        messages.success(request, "Your password has been successfully changed.")
        return redirect('login')

    return render(request, 'ForgetPassword.html')


    
    





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

