
from django.contrib import admin
from django.urls import path, include
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hellow/', view.helloworldfunction),
    path('', view.HelloWorldClass.as_view()), 
    path('helloapp/', include('helloapp.urls')),
    
]
