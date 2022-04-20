from django.shortcuts import render,redirect
from .forms import InputForm, LoginForm
from .models import Series, test_database1
from django.contrib.auth.views import LoginView,LogoutView
from .func1 import delete_database, input_database,input_database2, print_database,print_database2, seiri_database, type_print
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'WorkApp/home.html')

@login_required
def page1(request):
    return render(request, 'WorkApp/page1.html')

@login_required
def graph1(request):
    dicton = seiri_database()
    
    return render(request, 'WorkApp/graph1.html', {'dict':dicton})

@login_required
def graph2(request):
    dict = type_print()
    return render(request, 'WorkApp/graph2.html',{'dict':dict})

@login_required
def graph3(request):
    df = print_database()
    dict = df.to_dict('records')
    return render(request, 'WorkApp/graph3.html',{'dict':dict})

@login_required
def page4(request):
    return render(request, 'WorkApp/page4.html')


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
        if 'price' in request.POST:
            input_database(id,series,syusai,start_day,end_day,price)
            df = print_database()
            dict = df.to_dict('records')
        else:
            delete_database('r4table_2',id)
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
    type = request.POST.get('type')
    memo = request.POST.get('memo')
    df = print_database2()
    dict = df.to_dict('records')
    if request.method=='POST':
        if 'price' in request.POST:
            input_database2(id,title,furikomi,furikomi_day,price,type,memo)
            df = print_database2()
            dict = df.to_dict('records')
        else:
            delete_database('r4table2',id)
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