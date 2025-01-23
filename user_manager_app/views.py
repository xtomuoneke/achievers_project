from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def Register(request):
    if request.method == 'POST':                                                                                                                                          
        first_name = request.POST.get('fist_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        date_of_birth = request.POST.get(date_of_birth)

        user_data_has_error = False

        if User.objects.filter(username=username).exists():
             user_data_has_error = True
             messages.error(request, "Username already exist")

        if User.objects.filter(email=email).exists():
             user_data_has_error = True
             messages.error(request, "Email already exist")

        if len(password) < 5:
           user_data_has_error = True
           messages.error(request, "Password must be at least five characters")
        
        if  user_data_has_error:
            return redirect('register')
        else:
            new_user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
                password=password
            )
            messages.success(request, "Account created")
            return redirect('login')


    return render(request, 'learn/register.html')
  
