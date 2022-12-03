from django.db import models
from django.core.validators import FileExtensionValidator

class Video(models.Model):
    title=models.CharField('動画タイトル', max_length=255)
    thumbnail=models.ImageField('動画サムネイル', blank=True)
    file=models.FileField(
        '動画ファイル',
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'mpeg', 'mpg', 'avi', 'wmv', 'flv', ''])]
    )

    def __str__(self):
        return self.title

# Create your models here.
