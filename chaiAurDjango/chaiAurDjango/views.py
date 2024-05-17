from django.http import HttpResponse

def home(request):
    return HttpResponse("This is Home Page ;)")

def about(request):
    return HttpResponse("This is About Page ;)")

def contacts(request):
    return HttpResponse("This is Contacts Page ;|")