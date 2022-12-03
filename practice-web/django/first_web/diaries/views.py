from django.shortcuts import render
from .models import Diary

def top(request):
    context={
        'diary_list':Diary.objects.all(),
    }
    return render(request, 'diaries/diary_list.html', context)

# Create your views here.
