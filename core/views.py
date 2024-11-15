from django.shortcuts import render, redirect
from core.models import PatientAppoint, PatientQuery
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def appointment(request):
    return render(request, 'appointment.html')

def about(request):
    return render(request, 'about.html')

def book_appointment(request):
    if request.method == "POST":
        yourname = request.POST.get('yourname')
        youremail = request.POST.get('youremail')
        yourmobile = request.POST.get('yourmobile')
        yourdoctor = request.POST.get('yourdoctor')
        yourdate = request.POST.get('yourdate')
        yourtime = request.POST.get('yourtime')
        problem = request.POST.get('problem')
        if not yourmobile.isdigit() or len(yourmobile) < 10 or yourmobile == "":
            messages.error(request, 'Please enter a valid 10-digit mobile number.')
            return redirect('appointment')

        new_patient = PatientAppoint(yourname=yourname, youremail=youremail, yourmobile=yourmobile, 
                                     yourdoctor=yourdoctor, yourdate=yourdate, yourtime=yourtime, 
                                     problem=problem)
        new_patient.save()

        # confirmation email send

        template = render_to_string('email.html',{'username':yourname, 'doc':yourdoctor, 'date':yourdate, 'time':yourtime,})
        email = EmailMessage(
        'Appointment booking confirmation!', template, settings.EMAIL_HOST_USER, [youremail],
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


    