from django.db import models
from django.urls import reverse
from main_app.models import Patient, Service

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    patient = models.ForeignKey(Patient, default=None, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, default=None, on_delete=models.CASCADE)
    description=models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
    
    
    