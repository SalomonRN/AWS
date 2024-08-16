from django.http import HttpRequest
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .forms import *
from .models import *
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def cita(request:HttpRequest):
    if request.method == "POST":
        cita = CitaForm(request.POST)
        if not cita.is_valid():
            return HttpResponse(cita.errors)
        cita.save()
        return redirect('agendada')
    elif request.method == "GET":
        print("request.session------------------------")
        print(request.session)
        print(request.user.is_authenticated)
        form = CitaForm()
        
        #pets = Mascota.objects.get(id=id)
        pets = None
        return render(request, "cita.html", {"form": form, "pets_owner": pets})

    
def doctor(request: HttpRequest):
    return render(DoctorForm())

def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('veterinaria:home')
    else:
        form = LoginForm()
    return render(request, 'index.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('veterinaria:login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

@login_required(login_url='/cita/')
def home(request):
    return HttpResponse("HOLA LOGIN")


@login_required(login_url='/cita/?next=%s')
def logout(request):
    auth_logout(request)
    return redirect('login')