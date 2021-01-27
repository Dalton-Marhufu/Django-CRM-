from django.db import models
from django.contrib.auth.models import AbstractUser


# User model
class User(AbstractUser):
    pass

# sales leads
class Leads(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    phoned = models.BooleanField(default=False)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

# Agent model
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)



