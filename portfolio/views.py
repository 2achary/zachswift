from django.shortcuts import render
from twilio.rest import TwilioRestClient

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def resume(request):
    return render(request, 'resume.html')

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

def sms(fromnum, body):

    account_sid = "AC5d7ec2b523b18b015df1e251394e0c62"
    auth_token  = "c56a669bfcbe7c2ac8e27f0ff4268950"
    client = TwilioRestClient(account_sid, auth_token)
    if "gym" in body.lower():
        msg = "13579#"
        message = client.messages.create(body=msg, to=fromnum, from_='+16155490818')
        return message.sid
    else:
        msg = "Didn't recognize that command."
        message = client.messages.create(body=msg, to=fromnum, from_='+16155490818')
        return message.sid



