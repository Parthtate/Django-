from django.shortcuts import render
from .models import ChaiVarity

# Create your views here.
# Step1: before define methods, go to settings and go into the INSTALLEAPPS and add chaiapp

def all_chai(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'chaiapp/all_chai.html', {'chais': chais})
