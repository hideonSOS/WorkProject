from django.shortcuts import render,redirect
from .forms import InputForm
from .models import Series, test_database1
from django.contrib.auth.views import LoginView,LogoutView


def home(request):
    return render(request, 'WorkApp/home.html')

def page1(request):
    return render(request, 'WorkApp/page1.html')

def input(request):
    #form = InputForm()
    #return render(request, 'mlapp/input_form.html', {'form':form})

    if request.method == "POST":            # Formの入力があった時、
        form = InputForm(request.POST)      # 入力データを取得する。
        if form.is_valid():                 # Formの記載の検証を行い、
            form.save()                     # 問題なければ、入力データを保存
            return redirect('page1')        # 保存後遷移するページの指定
    else:
        form = InputForm()
        return render(request, 'WorkApp/input.html', {'form':form})
        
def return_database1(request):
    database1=test_database1.objects.all()
    Serieson = Series.objects.all()
    database = {
        'database1':database1,
        'Series':Serieson
    }
    return render(request, 'WorkApp/output.html', {'database':database})



class Logout(LogoutView):
    template_name='WorkApp/logout.html'