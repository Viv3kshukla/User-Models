from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    USER_CHOICES=(
        ('A','userA'),
        ('B','userB'),
        ('C','userC')
    )

    user_type=models.CharField(max_length=20,choices=USER_CHOICES,default='C')

class UserDetails(models.Model):
    type=models.OneToOneField('CustomUser')
    extra_info=models.CharField(max_length=20)
