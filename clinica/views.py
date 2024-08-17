from django.contrib.admin.views.decorators import staff_member_required
from django.core.exceptions import ObjectDoesNotExist 
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .forms import *
from .models import *
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
# Create your views here.

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

@login_required(login_url='/')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='/')
def logout(request):
    auth_logout(request)
    return redirect('veterinaria:login')

@login_required(login_url='/')
def cita(request:HttpRequest):
    if request.method == "POST":
        cita = CitaForm(request.POST)
        if not cita.is_valid():
            return HttpResponse(cita.errors)
        cita.save()
        return redirect('veterinaria:home')
    elif request.method == "GET":
        form = CitaForm(client_id=request.session['_auth_user_id'])
        return render(request, "cita.html", {"form": form,})

def pet(request:HttpRequest):
    if request.method == "POST":
        pet = MascotaForm(request.POST)
        if not pet.is_valid():
            return HttpResponse(pet.errors)
        pet.save()
        return redirect('veterinaria:home')
    elif request.method == "GET":
        form = MascotaForm(client_id=request.session['_auth_user_id'])
        return render(request, "pet.html", {"form": form,})

@login_required(login_url='/')
def citas(request):
    citas = Cita.objects.filter(client=User.objects.get(id=request.session['_auth_user_id']))

    return render(request, "citas.html", {"citas": citas})

@login_required
@staff_member_required
def doctor(request: HttpRequest):
    form = DoctorForm()
    return render(request, 'doc.html', {"form": form})
