from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("this is home page")
def contact(request):
    return HttpResponse("this is contact page")
def about(request):
    return HttpResponse("this is about page")