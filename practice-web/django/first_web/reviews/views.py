from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from .forms import ReviewCreateForm
from django.views import generic
from django.urls import reverse_lazy

class ReviewDelete(generic.DeleteView):
    model=Review
    success_url=reverse_lazy('reviews:review_list')

class ReviewUpdate(generic.UpdateView):
    model=Review
    form_class=ReviewCreateForm
    success_ulr=reverse_lazy('reveiws:review_list')

class ReviewCreate(generic.CreateView):
    model=Review
    form_class=ReviewCreateForm
    success_url=reverse_lazy('reviews:review_list')


class ReviewList(generic.ListView):
    model=Review


class ReviewDetail(generic.DetailView):
    model=Review


# Create your views here.
