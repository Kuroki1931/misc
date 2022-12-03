from django.shortcuts import render
from rest_framework import generics
from user import serializers

class CreateUserView(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer

# Create your views here.
