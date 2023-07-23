from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.models import User

# Create your views here.
def login_page(request): 
    if request.method=='POST':
        username = request.POST.get('username_field')
        password = request.POST.get('password_field')
        
        check_login  = authenticate(request , username = username , password=password)
        if not check_login:
            return HttpResponse("<h1> Incorrect Username password combination. Please Try again </h1>")
        
        login(request , check_login)
        return redirect('homepage')
        
    return render(request , 'login_page.html')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login_page')
    
def register_user(request):
    
    if request.method == 'POST':
        username = request.POST.get('username_field')
        password1 = request.POST.get('password_field1')
        password2 = request.POST.get('password_field2')
        email_address = request.POST.get('username_email')
        if password1 != password2:
            return HttpResponse("Password Mismatch")
        
        user_objs = User.objects.filter(username = username).values('id')
        if user_objs:
            return HttpResponse("User Already Exists")
        
        User.objects.create_user(username , email_address , password1)
        return redirect('homepage')
    return render(request , 'register_page.html')