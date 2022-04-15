from django.shortcuts import render,redirect
from .forms import InputForm
from .models import Series, test_database1
from django.contrib.auth.views import LoginView,LogoutView
from .func1 import delete_database, input_database


def home(request):
    return render(request, 'WorkApp/home.html')

def page1(request):
    return render(request, 'WorkApp/page1.html')

def page2(request):
    return render(request, 'WorkApp/page2.html')

def page3(request):
    return render(request, 'WorkApp/page3.html')

def page4(request):
    return render(request, 'WorkApp/page4.html')

# def input(request):
#     #form = InputForm()
#     #return render(request, 'mlapp/input_form.html', {'form':form})

#     if request.method == "POST":            # Formの入力があった時、
#         form = InputForm(request.POST)      # 入力データを取得する。
#         if form.is_valid():                 # Formの記載の検証を行い、
#             form.save()                     # 問題なければ、入力データを保存
#             return redirect('page1')        # 保存後遷移するページの指定
#     else:
#         form = InputForm()
#         return render(request, 'WorkApp/input.html', {'form':form})

        
# import pandas as pd
# from django_pandas.io import read_frame      
# def return_database1(request):
#     database1=test_database1.objects.all()
#     Serieson = Series.objects.all()
#     df = read_frame(Serieson)
#     print(df)
#     database = {
#         'database1':database1,
#         'Series':Serieson
#     }
#     return render(request, 'WorkApp/output.html', {'database':database})
def input(request):
    id = request.POST.get('id')
    series = request.POST.get('series')
    syusai = request.POST.get('syusai')
    start_day = request.POST.get('start_day')
    end_day = request.POST.get('end_day')
    price = request.POST.get('price')
    if request.method=='POST':
        input_database(id,series,syusai,start_day,end_day,price)
        # delete_database(id)
    
    return render(request,'WorkApp/input.html')


def output(request):
    return render(request, 'WorkApp/output.html')



class Logout(LogoutView):
    template_name='WorkApp/logout.html'

def delete(request):
    id = request.POST.get('id')
    if request.method=='POST':
        delete_database(id)
    return render(request, 'WorkApp/delete.html')