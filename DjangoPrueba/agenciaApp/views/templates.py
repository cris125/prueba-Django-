
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from rest_framework import status, views
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader




def loginHome(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def singup(request):
  template = loader.get_template('adduser.html')
  return HttpResponse(template.render())

def login(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())



  


