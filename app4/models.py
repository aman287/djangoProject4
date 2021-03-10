from django.db import models

class Account(models.Model):
    acno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=70)
    balance = models.DecimalField(max_digits=10,decimal_places=2)
    password = models.CharField(max_length=30)

def __str__(self):
    return self.ename=