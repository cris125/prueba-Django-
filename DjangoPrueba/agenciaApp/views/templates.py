from audioop import reverse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from rest_framework import status, views
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader

@login_required(login_url='/userlogin')  # Redirige a '/login' si el usuario no está autenticado
def loginHome(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render(request))



# Create your views here.
def redirect(request):
  return redirect('/login')

def singup(request):
  template = loader.get_template('adduser.html')
  return HttpResponse(template.render())

def login(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())





def login(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())
  


