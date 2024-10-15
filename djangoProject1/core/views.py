from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User


# Create your views here.

def HomePage(request):
    return render(request, 'home.html')

def AboutPage(request):
    return render(request, 'about.html')

def ContactPage(request):
    return render(request, 'contact.html')

def add_fav(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        food_id = data.get('id')
        User.favorite_food.update({food_id:name})
        return redirect('/')


def delete_url(request, id):
    queryset = User.objects.get(id=id)
    queryset.delete()
    return redirect('/')

