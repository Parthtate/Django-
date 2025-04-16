from django.shortcuts import render
from .models import ChaiVarity, Store
from .forms import ChaiVarityForm

# Create your views here.
# Step1: before define methods, go to settings and go into the INSTALLEAPPS and add chaiapp

def all_chai(request):
    chais = ChaiVarity.objects.all()
    return render(request, 'chaiapp/all_chai.html', {'chais': chais})

def store(request):
    stores = None
    if request.method == 'POST':
        form = ChaiVarityForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_variety']
            stores = Store.objects.filter(chai_varities=chai_variety)
    else: 
        form = ChaiVarityForm()        
    return render(request, 'chaiapp/store.html', {'stores': stores, 'form':form})
