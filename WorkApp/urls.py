from django.urls import path, include
from . import views


urlpatterns=[
    path('', views.home, name='home'),
    path('page1/', views.page1, name='page1'),
    path('graph1/', views.graph1, name='graph1'),
    path('graph2/', views.graph2, name='graph2'),
    path('graph3/', views.graph3, name='graph3'),
    path('input/', views.input, name='input'),
    path('input2/', views.input2, name='input2'),
    path('output/', views.output, name='output'),
    path('logout/', views.Logout.as_view(), name = 'logout'),
    path('mail/' ,views.mailon,name='mail'),
    path('login/', views.Login.as_view(), name='login'),
]
