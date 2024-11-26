from django.db import models
from django.conf import settings

# Create your models here.

class Transaction(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name='sent_transactions', on_delete=models.SET_NULL)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,  related_name='received_transactions', on_delete=models.SET_NULL)
    amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Histohy(models.Model):
    models.CharField(max_length=50)