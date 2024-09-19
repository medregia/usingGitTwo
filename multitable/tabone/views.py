from django.shortcuts import render, redirect
from django.http import HttpResponse

def tab_a(request):
    return HttpResponse('hi')
    
