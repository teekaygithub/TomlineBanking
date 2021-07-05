from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Account(models.Model):
    ACCOUNT_TYPES = (
        ('CH', 'Checking'),
        ('SA', 'Saving'),
        ('CC', 'Credit Card'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(default="Checking", max_length=100, choices=ACCOUNT_TYPES)
    date_created = models.DateTimeField(auto_now=True)
    date_deactivated = models.DateTimeField(blank=True, null=True)
    balance = models.IntegerField(default=1000)
    is_active = models.BooleanField(default=True)
    # transactions = models.ManyToManyField('Transactions')