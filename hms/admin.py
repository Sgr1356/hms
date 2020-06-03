from django.contrib import admin

# Register your models here.
from hms.models import doctormodel, patientmodel, appointmentmodel

admin.site.register(doctormodel)
admin.site.register(patientmodel)
admin.site.register(appointmentmodel)
