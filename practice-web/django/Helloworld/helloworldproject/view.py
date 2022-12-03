from django.http import HttpResponse
from django.views.generic import TemplateView

def helloworldfunction(request):
    returnedproject=HttpResponse('<h1>hello world</h1>')
    return returnedproject

class HelloWorldClass(TemplateView):
    template_name='hello.html'