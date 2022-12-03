from django.urls import path
from . import view

app_name='helloapp'

urlpatterns = [
    path('', view.helloappview)
    
]