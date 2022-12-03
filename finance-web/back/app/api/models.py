from django.db import models
import uuid
from django.contrib.postgres.fields import ArrayField
from django.db.models import JSONField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.core.validators import FileExtensionValidator

TYPE_CHOICES = (
        (0, 'simple_basic'),
        (1, 'deep'),
        (2, 'short'),
    )

def load_path_pdf(instance, filename):
    return '/'.join(['pdf', str(instance.title)+str(".pdf")])

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email address is must')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):

    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, editable=False)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

class Company(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, editable=False)
    company_name = models.CharField(max_length=30, blank=True)
    company_number = models.PositiveSmallIntegerField(
        verbose_name='',
        blank=True,
        default=0,
    )

    class Meta:
        ordering = ('company_number', ) 

    def __str__(self):
        return self.company_name + ' ' + str(self.company_number)

class PDF(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, editable=False)
    regist_date = models.DateTimeField(default=timezone.now)
    pdf_type = models.IntegerField(
        verbose_name="pdf_type",
        choices=TYPE_CHOICES)
    pdf_title = models.CharField(max_length=30, blank=True)
    pdf = models.FileField(
        blank=True, 
        upload_to='pdf',
        validators=[FileExtensionValidator(['pdf',])],
        )
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('company', 'pdf_type', '-regist_date' ) 

    def __str__(self):
        return self.company.company_name + ' ' + self.pdf_title

class Question(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, editable=False)
    question = models.CharField(max_length=500, blank=True)
    title = models.CharField(max_length=50, blank=True)
    regist_date = models.DateTimeField(default=timezone.now)
   

    class Meta:
        ordering = ('regist_date', ) 

    def __str__(self):
        return self.title + ' ' + str(self.regist_date)

class Ask(models.Model):
    id = models.UUIDField(default=uuid.uuid4,
                          primary_key=True, editable=False)
    askto = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    ask = models.CharField(max_length=500, blank=True)
    regist_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('regist_date', ) 

    def __str__(self):
        return self.askto.title + ' ' + str(self.regist_date)