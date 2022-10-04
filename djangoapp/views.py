# -*- coding: utf-8 -*-

from django.shortcuts import render

# Create your views here.

def home(request):
  return render(request, 'djangoapp/shell.html')


def err404(request):
  return render(request, 'djangoapp/404.html')

def comp1(request):
  return render(request, 'djangoapp/comp1.html')

def comp2(request):
  return render(request, 'djangoapp/comp2.html')