from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, World!. This is Home Page, Welcome to Python with Django framework")
    return render(request, 'website/index.html')

def about(request):
   # return HttpResponse("Django is a python framework, use for develop and builing fast paced web-application")
   return render(request, 'website/about.html')

def contact(request):
    # return HttpResponse("You you want to try this framework, search django framework on internet.")
    return render(request, 'website/contact.html')
