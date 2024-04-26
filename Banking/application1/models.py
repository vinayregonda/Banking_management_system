from django.db import models
from datetime import datetime

class Account(models.Model):
    accountNumber = models.CharField(max_length=20, null=False, blank=False)
    firstName = models.CharField(max_length=20, null=False, blank=False)
    middleName = models.CharField(max_length=20, null=True, blank=True)
    lastName = models.CharField(max_length=20, null=False, blank=False)
    Email = models.EmailField()
    Password = models.CharField(max_length=20, null=False, blank=False)
    Pin = models.IntegerField(null=False, blank=False)
    beginingBalance = models.IntegerField(null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    last_update = models.DateTimeField(default=datetime.now, blank=True)
class Announcement(models.Model):
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    title = models.CharField(max_length=25, null=False, blank=False)
    body = models.CharField(max_length=225, null=False, blank=False)
    last_date  = models.DateTimeField(default=datetime.now, blank=True)

class Transactions(models.Model):
    account_id = models.CharField(max_length=20, null=False, blank=False)
    Transaction_type = models.CharField(max_length=30, null=False, blank=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    Amount = models.IntegerField(null=True, blank=True)


    
