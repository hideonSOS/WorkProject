from django.shortcuts import render
from .forms import InputForm
def home(request):
    return render(request, 'WorkApp/home.html')

def page1(request):
    return render(request, 'WorkApp/page1.html')

def input(request):
    form = InputForm()
    
    return render(request, 'WorkApp/input.html', {'form':form})