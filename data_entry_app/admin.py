from django.contrib import admin
from .models import AbstractUser,Event,HealthInstitution,Profession


# Register your models here.
admin.site.register(Event)
admin.site.register(HealthInstitution)
admin.site.register(Profession)