from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from core.models import PatientAppoint, PatientQuery, Newsletter
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def appointment(request):
    return render(request, 'appointment.html')

def about(request):
    return render(request, 'about.html')

# signin signup

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']   

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        messages.success(request, 'successful!')
        return redirect('signin')

    return render(request, 'authentication/signup.html')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']

        user = authenticate(username=username, password=password1)

        if user is not None:
            login(request, user)
            messages.success(request, 'hello!')
            return redirect('home')

        else:
            messages.error(request, 'Not applicable!')
            return redirect('home')

    return render(request, 'authentication/signin.html')


def book_appointment(request):
    if request.method == "POST":
        yourname = request.POST.get('yourname')
        youremail = request.POST.get('youremail')
        yourmobile = request.POST.get('yourmobile')
        yourdoctor = request.POST.get('yourdoctor')
        yourdate = request.POST.get('yourdate')
        yourtime = request.POST.get('yourtime')
        problem = request.POST.get('problem')

        new_patient = PatientAppoint(
            yourname=yourname, 
            youremail=youremail, 
            yourmobile=yourmobile, 
            yourdoctor=yourdoctor, 
            yourdate=yourdate, 
            yourtime=yourtime, 
            problem=problem,
        )
        
        new_patient.save()

        # confirmation email send

        template = render_to_string(
            'email.html',
            {'username':yourname, 'doc':yourdoctor, 'date':yourdate, 'time':yourtime,}
        )

        email = EmailMessage(
            'Appointment booking confirmation!', 
            template, 
            settings.EMAIL_HOST_USER, 
            [youremail],
        )
        email.fail_silently = False
        email.send()

        return render(request, 'success.html', {
                                                'yourname':yourname,
                                                'youremail':youremail,
                                                'yourmobile':yourmobile,
                                                'yourdoctor':yourdoctor,
                                                'yourdate':yourdate,
                                                'yourtime':yourtime,
                                                'problem':problem})
    else:
        return render(request, 'appointment.html')

def home(request):
    return render(request, 'index.html')

def team(request):
    return render(request, 'team.html')

def service(request):
    return render(request, 'service.html')

def feature(request):
    return render(request, 'feature.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def contact(request):
    return render(request, 'contact.html')

def query(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        new_query = PatientQuery(name=name, email=email, subject=subject, message=message)
        new_query.save()
        messages.success(request, 'query received!')
        return redirect('home')
    else:
        return render(request, 'contact.html')   

def newsletter(request):
    if request.method == "POST":
        newemail = request.POST.get('newemail')

        new_email = Newsletter(newemail=newemail)
        new_email.save()
        messages.success(request, 'email registered!')
        return redirect('home')
    else:
        return render(request, 'index.html')






    