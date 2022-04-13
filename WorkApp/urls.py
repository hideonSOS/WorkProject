from django.urls import path, include
from . import views


urlpatterns=[
    path('', views.home, name='home'),
    path('page1/', views.page1, name='page1'),
    path('page2/', views.page2, name='page2'),
    path('page3/', views.page3, name='page3'),
    path('page4/', views.page4, name='page4'),
    path('input/', views.input, name='input'),
    path('output/', views.return_database1, name='output'),
    path('logout/', views.Logout.as_view(), name = 'logout'),
    
]
