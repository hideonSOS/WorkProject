from django.shortcuts import render,redirect
from .forms import InputForm, LoginForm
from .models import Series, test_database1
from django.contrib.auth.views import LoginView,LogoutView
from .func1 import delete_database, input_database,input_database2, print_database,print_database2, seiri_database
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'WorkApp/home.html')

@login_required
def page1(request):
    return render(request, 'WorkApp/page1.html')

@login_required
def page2(request):
    dicton = seiri_database()
    
    return render(request, 'WorkApp/page2.html', {'dict':dicton})

@login_required
def page3(request):
    df = print_database()
    dict = df.to_dict('records')
    
    return render(request, 'WorkApp/page3.html',{'dict':dict})

@login_required
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
@login_required
def input(request):
    id = request.POST.get('id')
    series = request.POST.get('series')
    syusai = request.POST.get('syusai')
    start_day = request.POST.get('start_day')
    end_day = request.POST.get('end_day')
    price = request.POST.get('price')
    df = print_database()
    dict = df.to_dict('records')
    if request.method=='POST':
        input_database(id,series,syusai,start_day,end_day,price)
        # delete_database(id)
        df = print_database()
        dict = df.to_dict('records')
    
    return render(request,'WorkApp/input.html',{'dict':dict})

@login_required
def input2(request):
    id = request.POST.get('id')
    title = request.POST.get('title')
    furikomi=request.POST.get('furikomi')
    furikomi_day=request.POST.get('furikomi_day')
    price = request.POST.get('price')
    memo = request.POST.get('memo')
    df = print_database2()
    dict = df.to_dict('records')
    if request.method=='POST':
        input_database2(id,title,furikomi,furikomi_day,price,memo)
        df = print_database2()
        dict = df.to_dict('records')
    return render(request, 'WorkApp/input2.html',{'dict':dict})


@login_required
def output(request):
    return render(request, 'WorkApp/output.html')



class Logout(LogoutView):
    template_name='WorkApp/logout.html'


class Login(LoginView):
    form_class=LoginForm
    template_name = 'WorkApp/login.html'

@login_required
def delete(request):
    df = print_database()
    dict = df.to_dict('records')
    id = request.POST.get('id')
    if request.method=='POST':
        delete_database(id)
        df = print_database()
        dict = df.to_dict('records')
    return render(request, 'WorkApp/delete.html',{'dict':dict})