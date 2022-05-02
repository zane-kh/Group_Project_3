from django.db import models
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
GENDERS_CHOICE = (
    ('F', 'Female'),
    ('M', 'Male')
)

class Patient(models.Model):
    patient_name = models.CharField(max_length=50)
    patient_lastname = models.CharField(max_length=50)
    patient_species = models.CharField(max_length=50)
    patient_age = models.IntegerField()
    patient_gender = models.CharField(
        max_length=1,
        choices=GENDERS_CHOICE
    )
    patient_weight = models.IntegerField()
    color = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.patient_name

    def get_absolute_url(self):
        return reverse('patient_history', kwargs={'patient_id': self.id})

class Service(models.Model):
    service_price = models.IntegerField()
    service_type = models.CharField(max_length=50)
    service_duration = models.DurationField()
    service_description = models.TextField(max_length=200)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.service_type
    
    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'pk': self.id})
