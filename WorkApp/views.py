from django.shortcuts import render,redirect
from .forms import InputForm, LoginForm
from .models import Series, test_database1
from django.contrib.auth.views import LoginView,LogoutView
from .func1 import delete_database, input_database,input_database2, print_database,print_database2, seiri_database, type_print
from . import func1
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'WorkApp/home.html')

@login_required
def page1(request):
    # df = func1.seiri_database2()
    import pandas as pd
    import numpy as np
    df = pd.read_excel('WorkApp\static\WorkApp\database_excel.xlsx',index_col=0)
    dict={
        'one':df.to_dict(orient='records'),
        'two':np.unique(df['furikomi']),
        'three':np.unique(df['type']),
        'four':df.to_dict(orient='records'),
    }

    if request.method=='POST':
        #1つ目のボタンを押したら
        if 'day' in request.POST:
            start_day = request.POST.get('start_day')
            end_day = request.POST.get('end_day')
            df1=df[(df['furikomi_day']>=start_day)&(df['furikomi_day']<=end_day)]
            dicton = {
                'one':df.to_dict(orient='records'),
                'two':np.unique(df['furikomi']),
                'three':np.unique(df['type']),
                'four':df1.to_dict(orient='records'),
                'five':f'{start_day} >>> {end_day} 期間での抽出結果'
            }

            return render(request, 'WorkApp/page1.html',{'html_dict':dicton})

        elif 'list1' in request.POST:
            list1_value = request.POST.get('liston1')
            df1 = df[df['furikomi']==list1_value]
            dicton1 = {
                'one':df.to_dict(orient='records'),
                'two':np.unique(df['furikomi']),
                'three':np.unique(df['type']),
                'four':df1.to_dict(orient='records'),
                'five':f'{list1_value} での抽出結果'
            }
        
            return render(request, 'WorkApp/page1.html',{'html_dict':dicton1})
            
        elif 'list2' in request.POST:
            list2_value=request.POST.get('liston2')
            df1 = df[df['type']==list2_value]
            dicton2={
                'one':df.to_dict(orient='records'),
                'two':np.unique(df['furikomi']),
                'three':np.unique(df['type']),
                'four':df1.to_dict(orient='records'),
                'five':f'{list2_value} での抽出結果'
            }
            
            return render(request, 'WorkApp/page1.html',{'html_dict':dicton2})

    return render(request, 'WorkApp/page1.html',{'html_dict':dict})
    
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
            delete_database('r4table',id)
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
            delete_database('r4table_2',id)
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
def mailon(request):
    from . import mail,mail_body
    #送信先１
    to_email1 = "hideo.code1555@gmail.com"
    #送信先２
    to_email2 = "code1555@icloud.com"
    to_email3 = "a-hoshino@and-ai.jp"
    to_email4 = "and-ai@nifty.com"

    subjecton=request.POST.get('texteria1')
    # messageon=request.POST.get('texteria2')
    # pathlist=request.POST.get('fileon')
    #もしラジオボタンでアンドアイが選択されていたら
    if request.method=="POST" and request.POST.get('select')=='andai':
        if 'select1' in request.POST:
            testlist = request.FILES.getlist('fileon')
            messageon=mail_body.andai_send()
            mail.send_pdf(subjecton,messageon,testlist,to_email1)
            print('test_send')
        elif 'select2' in request.POST:      
            testlist = request.FILES.getlist('fileon')
            messageon=mail_body.andai_send()
            mail.send_pdf(subjecton,messageon,testlist,to_email3)
            mail.send_pdf(subjecton,messageon,testlist,to_email4)
            print('test_send')
    else:
        print('else')
        # testlist = request.FILES.getlist('fileon')
        # messageon=mail_body.andai_send()
        # mail.send_image(subjecton,messageon,testlist,to_email1)
    return render(request, 'WorkApp/mail.html')