from django.contrib import admin
from .models import Diary, Category, CreatedAt

admin.site.register(Diary)
admin.site.register(Category)
admin.site.register(CreatedAt)
# Register your models here.
