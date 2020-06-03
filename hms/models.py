
from django.db import models

# Create your models here.
class doctormodel(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    contact = models.IntegerField(unique=True)
    speciality = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class patientmodel(models.Model):
    name = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    contact = models.IntegerField(unique=True)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class appointmentmodel(models.Model):
    doctor = models.ForeignKey(doctormodel, on_delete=models.CASCADE)
    patient = models.ForeignKey(patientmodel, on_delete=models.CASCADE)
    date1 = models.DateField()
    time1 = models.TimeField()

    def __str__(self):
        return self.doctor.name + "--" + self.patient.name
