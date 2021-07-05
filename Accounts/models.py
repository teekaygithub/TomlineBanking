from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(default="Checking", max_length=100)
    date_created = models.DateTimeField(auto_now=True)
    date_deactivated = models.DateTimeField(blank=True, null=True)
    balance = models.IntegerField(default=1000)
    is_active = models.BooleanField(default=True)
    # transactions = models.ManyToManyField('Transactions')