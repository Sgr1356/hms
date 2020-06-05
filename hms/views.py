from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import doctormodel,patientmodel,appointmentmodel


# Create your views here.


def about(request):
    return render(request, "about.html")


def index(request):
    if not request.user.is_staff:
        return redirect('login')
    doctors =  doctormodel.objects.all()
    patients =  patientmodel.objects.all()
    appointments =  appointmentmodel.objects.all()

    d = 0;
    p = 0;
    a = 0;
    for i in doctors:
        d+=1
    for i in patients:
        p+=1
    for i in appointments:
        a+=1
    d1 = {'d':d,'p':p,'a':a}
    return render(request, "index.html",d1)


def Login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request,"login.html",d)


def logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')


def contact(request):
    return render(request,"contact.html")


def view_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = doctormodel.objects.all()
    d = {'doc':doc}
    return render(request,'view_doctor.html',d)

def add_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    error = ""
    if request.method == 'POST':
        na = request.POST['name']
        ls = request.POST['last']
        cnt = request.POST['contact']
        sp = request.POST['special']
        try:
            doctormodel.objects.create(name=na,lastname=ls,contact=cnt,speciality=sp)
            error = "no"

        except:
            error = "yes"
    d = {'error': error}
    return render(request,"add_doctor.html",d)

def delete_doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = doctormodel.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')

#for patient

def view_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat = patientmodel.objects.all()
    d = {'pat':pat}
    return render(request,'view_patient.html',d)

def add_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    error = ""
    if request.method == 'POST':
        na = request.POST['name']
        ls = request.POST['last']
        gen = request.POST['gender']
        cnt = request.POST['contact']
        add = request.POST['address']
        try:
            patientmodel.objects.create(name=na,lastname=ls,gender=gen,contact=cnt,address=add)
            error = "no"

        except:
            error = "yes"
    d = {'error': error}
    return render(request,"add_patient.html",d)

def delete_patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = patientmodel.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')

#for Appointment

def view_appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    appoint = appointmentmodel.objects.all()
    d = {'appoint':appoint}
    return render(request,'view_appointment.html',d)

def add_appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = doctormodel.objects.all()
    patient1 = patientmodel.objects.all()

    if request.method == 'POST':
        d = request.POST['doctor']
        p = request.POST['patient']
        d1 = request.POST['date']
        t = request.POST['time']
        doctor = doctormodel.objects.filter(name=d).first()
        patient = patientmodel.objects.filter(name=p).first()

        try:
            appointmentmodel.objects.create(doctor=doctor, patient=patient, date1=d1, time1=t)
            error = "no"

        except:
            error = "yes"
    d = {'doctor': doctor1, 'patient': patient1, 'error': error}
    return render(request, "add_appointment.html", d)

def delete_appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    appointment = appointmentmodel.objects.get(id=pid)
    appointment.delete()
    return redirect('view_appointment')
