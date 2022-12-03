from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CompanySerializer
from .models import Company
from rest_framework.permissions import AllowAny

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
