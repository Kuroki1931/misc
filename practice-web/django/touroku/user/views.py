from django.shortcuts import render
from .forms import UserForm

def new(request):
    params = {'message': 'newです'}
    return render(request, 'user/new.html', params)

def new(request):
    params = {'name': '', 'email': '', 'form': None}
    if request.method == 'POST':
        form = UserForm(request.POST)
        params['name'] = request.POST['name']
        params['email'] = request.POST['email']
        params['form'] = form
    else:
        params['form'] = UserForm()
    return render(request, 'user/new.html', params)

# Create your views here.
