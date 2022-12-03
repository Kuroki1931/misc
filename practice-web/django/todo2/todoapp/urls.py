
from django.contrib import admin
from django.urls import path, include
from . import views

app_name='list'

urlpatterns = [
   path('', views.TodoList.as_view()),
   path('detail/<int:pk>', views.TodoDetail.as_view()),
]
