from django.shortcuts import render

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
