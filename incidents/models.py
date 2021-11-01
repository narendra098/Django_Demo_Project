from django.db import models

# Create your models here.
class Report(models.Model):
    location = models.CharField(max_length=100)
    Incident_Dept = models.CharField(max_length=100)
    dateandtime = models.DateTimeField()
    incident_location = models.TextField(max_length=500)
    initial_severity = models.CharField(max_length=100)
    suspected_cause = models.TextField(max_length=500)
    immediate_action_taken = models.TextField(max_length=500)
    sub_incident_type = models.CharField(max_length=100)
