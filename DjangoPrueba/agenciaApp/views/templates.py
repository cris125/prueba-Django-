from audioop import reverse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from rest_framework import status, views

from django.contrib import messages

# Create your views here.

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render())
def xd(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render())
  


