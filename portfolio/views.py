from django.shortcuts import render
from twilio.rest import TwilioRestClient
from django_twilio.decorators import twilio_view
from twilio.twiml import Response
from .models import Profile, Python, Web, WorkHistory, Contact, Education, General, OS, Deployment, Testing
from dateutil.parser import parse
import datetime

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def resume(request):
    tagline = Profile.objects.all()[0].tagline
    libraries = ', '.join([obj.library for obj in Python.objects.all()])
    web = ', '.join([obj.lang for obj in Web.objects.all()])
    contact = Contact.objects.all()[0]
    general = ', '.join([obj.name for obj in General.objects.all()])
    deployment = ', '.join([obj.name for obj in Deployment.objects.all()])
    testing = ', '.join([obj.name for obj in Testing.objects.all()])
    os = ', '.join([obj.name for obj in OS.objects.all()])
    work = WorkHistory.objects.order_by('-start_date')
    for obj in work:
        obj.title = obj.title.upper()
        obj.company = obj.company.upper()
        obj.location = obj.location.upper()
        obj.start_date = obj.start_date.strftime('%B %Y').upper()
        if obj.end_date:
            obj.end_date = obj.end_date.strftime('%B %Y').upper()

    education = Education.objects.order_by('-start_date')
    for obj in education:
        obj.start_date = obj.start_date.strftime('%Y').upper()
        if obj.end_date:
            obj.end_date = obj.end_date.strftime('%Y').upper()

    return render(request, 'resume.html', {
        'tagline': tagline,
        'libraries': libraries,
        'web': web, 'work': work,
        'contact': contact,
        'education': education,
        'general': general,
        'deployment': deployment,
        'testing': testing,
        'OS': os,

    })

def contact(request):
    return render(request, 'contact.html')

def lightbox(request):
    return render(request, 'lightbox.html')

def taskdaddy(request):
    return render(request, 'taskdaddy.html')

def spoiler(request):
    return render(request, 'spoiler.html')

def projects(request):
    return render(request, 'projects.html')

@twilio_view
def sms(request):

    body = request.GET.get('Body', '')
    if "gym" in body.lower():
        msg = "13579#"
        r = Response()
        r.message(msg)
        return r
    else:
        msg = "Didn't recognize that command."
        r = Response()
        r.message(msg)
        return r
    #
    # fromnum = "+" + request.GET.get("From")[2:]
    # account_sid = "AC5d7ec2b523b18b015df1e251394e0c62"
    # auth_token  = "c56a669bfcbe7c2ac8e27f0ff4268950"
    # client = TwilioRestClient(account_sid, auth_token)
    # if "gym" in request['Body'].lower():
    #     msg = "13579#"
    #     message = client.messages.create(body=msg, to=fromnum, from_='+16155490818')
    #     return message.sid
    # else:
    #     msg = "Didn't recognize that command."
    #     message = client.messages.create(body=msg, to=fromnum, from_='+16155490818')
    #     return message.sid
    #
    #
    #
