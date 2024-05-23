from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("This is Home Page ;)")
    return render(request,'website/index.html')

def about(request):
    return HttpResponse("This is About Page ;)")

def contacts(request):
    return HttpResponse("This is Contacts Page ;|")