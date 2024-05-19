from django.db import models
from . managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from PIL import Image


# Create your models here.

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)

    is_doctor = models.BooleanField(default=False, verbose_name='Are you a Doctor?')
    
    is_patient = models.BooleanField(default=False, verbose_name='Are you a Patient?')

    is_administrator = models.BooleanField(default=False, verbose_name='Are you a Administrator?')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    @property
    def get_name(self):
        return self.first_name+" "+self.last_name

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_pics', blank=True, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}  Profile'


class Subscription(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, unique=True)
    
    subscription_id = models.CharField(max_length=300)
    subscriber_name = models.CharField(max_length=300)

    subscription_plan = models.CharField(max_length=255)
    subscription_cost = models.CharField(max_length=255)

    is_active = models.BooleanField(default=False)

    subscription_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f'{self.subscriber_name} - {self.subscription_plan} subscription'    