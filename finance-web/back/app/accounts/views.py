from django.shortcuts import render
# PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteViewを追加
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'five/index.html', {})