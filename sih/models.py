from django.db import models
from django.utils import timezone

# Create your models here.
class datas(models.Model):
    customer_name=models.CharField(max_length=100)
    customer_address=models.TextField()
    customer_phonenumber=models.BigIntegerField()
    timestamp=models.DateTimeField(default=timezone.now)

