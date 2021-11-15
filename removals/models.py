from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    role = models.CharField(max_length=64, default="user")


class Jobs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="jobs")
    name = models.CharField(max_length=64, default="NAME")
    phone = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    pickup = models.CharField(max_length=128)
    delivery = models.CharField(max_length=128)
    final_cost = models.IntegerField()
    commission = models.DecimalField(max_digits=5,decimal_places=2, default=0)
    date = models.DateField()
    time = models.TimeField()
    pick_code = models.CharField(max_length=64)
    deliv_code = models.CharField(max_length=64)
    comment = models.TextField()
    mover = models.CharField(max_length=64)



