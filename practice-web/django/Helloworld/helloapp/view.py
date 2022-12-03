from django.shortcuts import render
from django.http import HttpResponse

def helloappview(request):
    return HttpResponse('app is called')

# Create your views here.
