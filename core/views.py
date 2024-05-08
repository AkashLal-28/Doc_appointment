from django.shortcuts import render

def appoint(request):
    if request.method == "POST":
        yourname = request.POST.get('yourname')
        youremail = request.POST.get('youremail')
        yourmobile = request.POST.get('yourmobile')
        mydate = request.POST.get('mydate')
        mytime = request.POST.get('mytime')
        problem = request.POST.get('problem')
    return render(request, 'appointment.html')

def about(request):
    return render(request, 'about.html')

def appointment(request):
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


