from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import todoModel
from django.urls import reverse_lazy

# Create your views here.
class TodoList(ListView):
    template_name='list.html'
    model=todoModel

class TodoDetail(DetailView):
    template_name='detail.html'
    model=todoModel

class TodoCreate(CreateView):
    template_name='create.html'
    model=todoModel
    fields=('title', 'memo', 'priority', 'duedate')
    success_url=reverse_lazy('list')

class TodoDelete(DeleteView):
    template_name='delete.html'
    model=todoModel
    success_url=reverse_lazy('list')

class TodoUpdate(UpdateView):
    template_name='update.html'
    model=todoModel
    fields=('title', 'memo', 'priority', 'duedate')
    success_url=reverse_lazy('list')s

