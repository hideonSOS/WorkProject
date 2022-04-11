from django.urls import path, include
from . import views


urlpatterns=[
    path('', views.home, name='home'),
    path('page1/', views.page1, name='page1'),
    path('input/', views.input, name='input'),
    path('database1/', views.return_database1, name='database1'),
    
]
