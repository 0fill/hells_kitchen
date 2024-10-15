from django.shortcuts import render


# Create your views here.

def HomePage(request):
    return render(request, 'home.html')

def AboutPage(request):
    return render(request, 'about.html')

def ContactPage(request):
    return render(request, 'contact.html')
