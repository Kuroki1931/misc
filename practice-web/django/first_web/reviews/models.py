from django.db import models
from django.utils import timezone

class Review(models.Model):
    STARS=(
        (1, '★'),
        (2, '★★'),
        (3, '★★★'),
        (4, '★★★★'),
        (5, '★★★★★'),

    )

    store_name=models.CharField('店名', max_length=255)
    title=models.CharField('タイトル', max_length=255)
    text=models.TextField('口コミサイト', blank=True)
    stars=models.IntegerField('星野数', choices=STARS)
    created_at=models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.title




# Create your models here.
