from django.db import models

CHOICE=(('danger', 'high'), ('warning', 'normal'), ('primary', 'low'))

class todoModel(models.Model):
    title=models.CharField(max_length=100)
    memo=models.TextField()
    priority=models.CharField(
        max_length=50,
        choices=CHOICE
    )
    duedate=models.DateField()

    def __str__(self):
        return self.title

    

# Create your models here.
