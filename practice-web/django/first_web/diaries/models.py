from django.db import models
from django.utils import timezone

class CreatedAt(models.Model):
    name=models.CharField('作成日', max_length=255)


class Category(models.Model):
    name=models.CharField('カテゴリ名', max_length=255)
    created_at=models.ForeignKey(CreatedAt, verbose_name='作成日', null=True, blank=True, on_delete=models.PROTECT)
    # created_at=models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.name

class Diary(models.Model):
    category=models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)
    text=models.TextField('本文')
    created_at=models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return 'カテゴリ:{} 本文:{}' .format(self.category, self.text[:10])
