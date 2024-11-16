from django.db import models

class PatientAppoint(models.Model):
    yourname = models.CharField(max_length=70)
    youremail = models.EmailField()
    yourmobile = models.IntegerField()
    yourdoctor = models.CharField(max_length=70)
    yourdate = models.DateField()
    yourtime = models.TimeField()
    problem = models.CharField(max_length=200)
    
class PatientQuery(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    subject = models.CharField(max_length=80)
    message = models.CharField(max_length=200)

class Newsletter(models.Model):
    newemail = models.EmailField()