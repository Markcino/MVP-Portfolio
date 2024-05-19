from django.shortcuts import render, redirect
from . forms import CreatePatientForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test

from django.http import HttpResponse, JsonResponse

# Create your views here.

def register(request):
    form = CreatePatientForm()

    if request.method == "POST":
        form = CreatePatientForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('do_login')
    else:
        form = CreatePatientForm()

    context = {'RegisterForm': form}

    return render(request, "account/register.html", context)

def do_login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user.is_active and user.is_administrator:
                login(request, user)
                return redirect('administrator-dashboard')
            
            if user.is_active and user.is_doctor == True:
                login(request, user)
                return redirect('doctor_dashboard')
            
            
            if user is not None and user.is_doctor == False and user.is_administrator == False and user.is_superuser == False and user.is_active == True:
                login(request, user)
                return redirect('patient_dashboard')
            
    context = {'LoginForm': form}
            
    return render(request, "account/login.html", context)

@login_required(login_url='do_login')
def do_logout(request):
    logout(request)
    return redirect('home')