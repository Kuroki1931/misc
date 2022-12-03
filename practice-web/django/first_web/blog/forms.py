from django import forms
from .models import Comment

class CommentCreateForm(forms.ModelForm):

    class Meta:
        model=Comment
        fields=('text',)
        widgets={
            'text':forms.Textarea(attrs={'class':'textrea'})
        }

# Create your tests here.
