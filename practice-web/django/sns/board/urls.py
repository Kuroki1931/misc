from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signupfunc, name='signup'),
    path('login/', views.loginfunc, name='login'),
    path('list/', views.listfunc, name='list'),
    path('logout/', views.logoutfunc, name='logout'),
    path('detail/<int:pk>', views.detailfunc, name='detail'),
    path('good/<int:pk>', views.goodfunc, name='good'),
    path('read/<int:pk>', views.readfunc, name='read'),
    path('create/', views.BoardCreate.as_view(), name='create'),

]
