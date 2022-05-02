from django.contrib import admin
from .models import Patient, Service

# Register your models here.

admin.site.register(Patient)
admin.site.register(Service)