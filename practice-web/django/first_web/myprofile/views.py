from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.
def top(request):
    context={'name':'颯'}
    return render(request, 'myprofile/top.html', context)

def resume(request):
    return render(request, 'myprofile/resume.html')