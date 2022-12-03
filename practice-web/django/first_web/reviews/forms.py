from django import forms
from .models import Review

class ReviewCreateForm(forms.ModelForm):

    class Meta:
        model=Review
        exclude = ('created_at',)

# Create your tests here.
