from django.shortcuts import render
from .forms import InputForm
from .models import test_database1


def home(request):
    return render(request, 'WorkApp/home.html')

def page1(request):
    return render(request, 'WorkApp/page1.html')

def input(request):
    form = InputForm()
    return render(request, 'WorkApp/input.html', {'form':form})

def return_database1(request):
    database1=test_database1.objects.all()
    return render(request, 'WorkApp/output.html', {'database1':database1})


#test