import os

from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *


# Create your views here.
from homepro.settings import EMAIL_HOST_USER


def index(request):
    return render(request, 'index.html')


def navbar(request):
    return render(request, 'navbar.html')


def register(request):
    if request.method == 'POST':
        a = regform(request.POST)
        if a.is_valid():
            nm = a.cleaned_data['name']
            em = a.cleaned_data['email']
            ph = a.cleaned_data['phone']
            ps = a.cleaned_data['password']

            b = regmodel(name=nm, email=em, phone=ph, password=ps)
            b.save()
            return redirect(login)
        else:
            return HttpResponse("failed")
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        a = logform(request.POST)
        if a.is_valid():
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            b = regmodel.objects.all()
            for i in b:
                eml = i.email
                request.session['email'] = i.email
                id = i.id
                if i.email == em and i.password == ps:
                    return render(request, 'emp_profile.html', {'eml': eml, 'id': id})
            else:
                return HttpResponse("login failed")

    else:
        return render(request, 'login.html')


def empprofile(request):
    return render(request, 'emp_profile.html')


def empupload(request,id):
    b=regmodel.objects.get(id=id)
    cn=b.name
    el=b.email
    if request.method == 'POST':
        a = empuploadform(request.POST, request.FILES)
        if a.is_valid():
            nm = a.cleaned_data['name']
            em = a.cleaned_data['email']
            sv = a.cleaned_data['services']
            lo = a.cleaned_data['location']
            ph = a.cleaned_data['phone']
            # im = a.cleaned_data['image']
            bi = a.cleaned_data['bio']

            b = empuploadmodel(name=nm, email=em, services=sv, location=lo, phone=ph,
                               bio=bi)
            b.save()

            return redirect(viewemp)
        else:

            return HttpResponse("Upload failed")
    else:
        return render(request, 'emp_upload.html', {'cn': cn, 'el': el})


def display_employees(request):
    employees = empuploadmodel.objects.all()

    return render(request, 'display_emp.html', {'employees': employees})


def editemp(request, id):
    a = empuploadmodel.objects.get(id=id)
    cn = a.name
    el = a.email
    if request.method == 'POST':
        a.name = request.POST.get('name')
        a.email = request.POST.get('email')
        a.services = request.POST.get('services')
        a.location = request.POST.get('location')
        a.phone = request.POST.get('phone')
        a.bio = request.POST.get('bio')

        a.save()
        return redirect(viewemp)

    return render(request, 'empedit.html', {'a': a, 'cn': cn, 'el': el})


def deleteemp(request, id):
    employee = empuploadmodel.objects.get(id=id)
    employee.delete()
    return redirect(viewemp)


def userreg(request):
    if request.method == 'POST':
        a = userregform(request.POST, request.FILES)
        if a.is_valid():
            fn = a.cleaned_data['fname']
            ln = a.cleaned_data['lname']
            em = a.cleaned_data['email']
            ph = a.cleaned_data['phone']
            ps = a.cleaned_data['password']

            b = userregmodel(fname=fn, lname=ln, email=em, phone=ph, password=ps)
            b.save()
            return redirect(userlogin)
        else:
            return HttpResponse("failed")
    else:
        return render(request, 'userregister.html')


def userlogin(request):
    if request.method == 'POST':
        a = userlogform(request.POST)
        if a.is_valid():
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            b = userregmodel.objects.all()
            for i in b:
                fnm = i.fname
                id = i.id

                if i.email == em and i.password == ps:
                    eml = i.email
                    request.session['email'] = i.email
                    return render(request, 'userprofile.html', {'fnm': fnm, 'id': id, 'eml':eml})
            else:
                return HttpResponse("login failed")

    else:
        return render(request, 'userlogin.html')


def userprofile(request):
    return render(request, 'userprofile.html')


def userupload(request,id):
    b=userregmodel.objects.get(id=id)
    fn=b.fname
    el=b.email
    if request.method == 'POST':
        a = useruploadform(request.POST)
        if a.is_valid():
            nm = a.cleaned_data['fname']
            em = a.cleaned_data['email']
            sv = a.cleaned_data['service']
            ph = a.cleaned_data['phone']
            lo = a.cleaned_data['location']

            b = useruploadmodel(fname=nm, email=em, service=sv, phone=ph, location=lo)
            b.save()

            return redirect(viewuser)
        else:

            return HttpResponse("Upload failed")
    else:
        return render(request, 'upload_service.html', {'fn': fn, 'el': el})


def displayuser(request):
    employees = useruploadmodel.objects.all()
    return render(request, 'userdisplay.html', {'employees': employees})


def viewemp(request):
    employees = empuploadmodel.objects.all()
    b = request.session['email']
    return render(request, 'viewemployee.html', {'employees': employees,'b':b})
#
# def viewemp(request):
#     employees = empuploadmodel.objects.all()
#
#     return render(request, 'viewemployee.html', {'employees': employees})


def viewuser(request):
    employees = useruploadmodel.objects.all()
    b = request.session['email']
    return render(request, 'viewuser.html', {'employees': employees, 'b':b})


def edituser(request, id):
    a = useruploadmodel.objects.get(id=id)
    cn = a.fname
    el = a.email
    if request.method == 'POST':
        a.fname = request.POST.get('fname')
        a.email = request.POST.get('email')
        a.services = request.POST.get('services')
        a.phone = request.POST.get('phone')
        a.location = request.POST.get('location')

        a.save()
        return redirect(viewuser)

    return render(request, 'edituser.html', {'a': a, 'cn': cn, 'el': el})


def deleteuser(request, id):
    employee = useruploadmodel.objects.get(id=id)
    employee.delete()
    return redirect(viewuser)


# def applyemp(request):
#     return render(request, 'applyemp.html')

def applyemp(request, id):
    b = useruploadmodel.objects.get(id=id)

    sv = b.service
    if request.method == 'POST':
        a = empapplyform(request.POST)
        if a.is_valid():
            nm = a.cleaned_data['name']
            em = a.cleaned_data['email']
            ag = a.cleaned_data['age']
            gn = a.cleaned_data['gender']
            ph = a.cleaned_data['phone']
            sr = a.cleaned_data['service']
            ex = a.cleaned_data['experience']

            b = empapplymodel(name=nm, email=em, age=ag, gender=gn, phone=ph, service=sr, experience=ex)
            b.save()
            subject = f"Application Successful"
            message = f"hi {nm}\n your application is applied successfully"
            email_from = EMAIL_HOST_USER
            send_mail(subject, message, email_from, [em])
            return render(request, "useralert.html")
        else:
            return HttpResponse("failed")
    else:
        return render(request, 'applyemp.html', {'sv': sv})


def applyuser(request, id):
    b = empuploadmodel.objects.get(id=id)

    sv = b.services
    if request.method == 'POST':
        a = userapplyform(request.POST)
        if a.is_valid():
            n = a.cleaned_data['name']
            em = a.cleaned_data['email']
            ad = a.cleaned_data['address']
            ph = a.cleaned_data['phone']
            sr = a.cleaned_data['service']

            b = userapplymodel(name=n, email=em, address=ad, phone=ph, service=sr)
            b.save()
            subject = f"Application Successful"
            message = f"hi {n}\n your application is applied successfully"
            email_from = EMAIL_HOST_USER
            send_mail(subject, message, email_from, [em])

            return render(request,"useralert.html")
        else:
            return HttpResponse("failed")
    else:
        return render(request, 'applyuser.html', {'sv': sv})


#
# def displayappliedemp(request, id):
#     a = empapplymodel.objects.all()
#     b = request.session['name']
#     name = []
#     service=[]
#     email=[]
#     gender=[]
#     phone=[]
#     experience=[]
#     id1=[]
#     for i in a:
#         id=i.id
#         id1.append(id)
#         nm=i.name
#         sv=i.service
#         em=i.email
#         gn=i.gender
#         ph=i.phone
#         ex=i.experience
#         name.append(nm)
#         service.append(sv)
#         email.append(em)
#         gender.append(gn)
#         phone.append(ph)
#         experience.append(ex)
#     mylist=zip(name,service,email,gender,phone,experience,id1)
#     return render(request,'view_appliedemployees.html',{'list':mylist,'b':b})


def viewappliedemployee(request):
    employees = empapplymodel.objects.all()
    return render(request, 'displayappliedemp.html', {'employees': employees})


def viewapplieduser(request):
    employees = userapplymodel.objects.all()
    return render(request, 'displayapplieduser.html', {'employees': employees})


def userwishlist(request, id):
    a = useruploadmodel.objects.get(id=id)

    b = userwishlistmodel(fname=a.fname, email=a.email, service=a.service, phone=a.phone, location=a.location)

    b.save()
    return redirect(userwishlistdisplay)


def userwishlistdisplay(request):
    employees = userwishlistmodel.objects.all()
    return render(request, 'userwishlistdisplay.html', {'employees': employees})


def removeuserwishlist(request, id):
    employee = userwishlistmodel.objects.get(id=id)
    employee.delete()
    return redirect(userwishlistdisplay)


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def empwishlist(request, id):
    a = empuploadmodel.objects.get(id=id)

    b = empwishlistmodel(name=a.name, email=a.email, services=a.services, location=a.location, phone=a.phone, bio=a.bio)

    b.save()
    return redirect(empwishlistdisplay)


def empwishlistdisplay(request):
    employees = empwishlistmodel.objects.all()
    return render(request, 'empwishlistdisplay.html', {'employees': employees})


def removeempwishlist(request, id):
    employee = empwishlistmodel.objects.get(id=id)
    employee.delete()
    return redirect(empwishlistdisplay)
