from django.db import models
import uuid
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField

# Create your models here.

class Company(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, editable=False)
    name = models.CharField(max_length=30, blank=True)
    category = models.CharField(max_length=30, blank=True)
    keywords = JSONField(blank=True, db_index=True, null=True)
    recruit = JSONField(blank=True, db_index=True, null=True)
    news = JSONField(blank=True, db_index=True, null=True)

    def __str__(self):
        return self.name