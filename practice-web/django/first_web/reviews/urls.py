"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

app_name='reviews'


urlpatterns = [
    path('', views.ReviewList.as_view(), name='review_list'),
    path('detail/<int:pk>', views.ReviewDetail.as_view(), name='review_detail'),
    path('create/', views.ReviewCreate.as_view(), name='review_create'),
    path('update/<int:pk>/', views.ReviewUpdate.as_view(), name='review_update'),
    path('delete/<int:pk>/', views.ReviewDelete.as_view(), name='review_delete'),
    ]

