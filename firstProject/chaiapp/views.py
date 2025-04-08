from django.shortcuts import render

# Create your views here.
# Step1: before define methods, go to settings and go into the INSTALLEAPPS and add chaiapp

def all_chai(request):
    return render(request, 'chaiapp/all_chai.html')
