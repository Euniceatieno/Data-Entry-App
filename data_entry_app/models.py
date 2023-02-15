from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


###############################################################
# User DB Table
###############################################################
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_site_user = models.BooleanField(default=False)


###############################################################
# Base Model DB Table
###############################################################
class BaseModel(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now, null=True)


###############################################################
# Health Institution DB Table
###############################################################
class HealthInstitution(BaseModel):
    name = models.CharField(max_length=50, unique=True, null=False)
    phone_number = models.CharField(max_length=50, unique=True, null=False)
    speciality = models.CharField(max_length=50, unique=True, null=False)
    location = models.CharField(max_length=50, unique=True, null=False)


###############################################################
# Professional Details DB Table
###############################################################
class Profession(BaseModel):
    name = models.CharField(max_length=50, unique=True, null=False)
    description = models.TextField(null=False)
    occupation = models.CharField(max_length=50, unique=True, null=False)


###############################################################
# Event Details DB Table
###############################################################
class Event(BaseModel):
    event_name = models.CharField(max_length=30, unique=True, null=False)
    location = models.CharField(max_length=30, null=False)
    description = models.TextField(null=False)
    event_date = models.DateTimeField(null=False)
