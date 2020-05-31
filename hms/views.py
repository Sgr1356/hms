from django.shortcuts import render,redirect
from django.contrib import messages
# from hms.models import docpatmodel
# Create your views here.
def home(request):
    return render(request,'home.html')


def contact(request):
    return render(request,"contact.html")

# #for login check
# def logincheck(request):
#     email = request.POST.get("email")
#     passwd = request.POST.get("password")
#     ty="doctor"
#     return None

def signup(request):
    n= request.POST.get("na")
    last = request.POST.get("la")
    cont = request.POST.get("c_n0")
    email = request.POST.get("em")
    passw = request.POST.get("ps")
    dc_pt = request.POST.get("d1")
    print(n,last,cont,email,passw,dc_pt)

    # doctor=docpatmodel(name=n,lastname=last,contact=cont,emailid=email,password=passw,type=dc_pt)
    return None