from logging import RootLogger
from django.db import models
from users.models import Users
import uuid
from datetime import datetime
from django.utils import timezone


class Transaction(models.Model):
    user = models.ForeignKey(
        Users, on_delete=models.CASCADE, related_name='user_transaction', blank=True)

    created = models.DateTimeField(auto_now_add=True)
    transaction_id = models.AutoField(primary_key=True)
    #transaction_name = models.CharField(max_length=100,default=uuid.uuid4)
    amount = models.FloatField(default=0)
    transaction_type = models.CharField(max_length=100, default="")

    def __str__(self):
        return str(self.transaction_type)

    class Meta:
        ordering = ['created']


class Balance(models.Model):
    user_balance = models.OneToOneField(
        Users, on_delete=models.CASCADE, related_name='user_balance')
    balance_id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    balance = models.FloatField(default=0)



    class Meta:
        ordering = ['created']
