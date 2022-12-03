from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from core.models import Memo
from rest_framework import viewsets
from .serializers import MemoSerializer

class MemoViewSet(viewsets.ModelViewSet):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class CreateMemo(generics.CreateAPIView):
    serializer_class = MemoSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)



# Create your views here.
