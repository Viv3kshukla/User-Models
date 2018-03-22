from django.db import models
from django.contrib.auth.models import User
# Create your models here.



USER_CHOICES = (
    ('driver','driver'),
    ('official','official'),
    ('person','person'),
)

class CustomUser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_CHOICES,default='driver')
    extra_info=models.CharField(max_length=20,blank=True,null=True)