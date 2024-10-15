from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse

from recipes.models import Recipe
from .models import User, User_Recipe


# Create your views here.

def HomePage(request):
    return render(request, 'home.html')

def AboutPage(request):
    return render(request, 'about.html')

def ContactPage(request):
    return render(request, 'contact.html')

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request,
                  'registration.html',
                  {'form': UserCreationForm()})

@login_required
def profile(request):
    return render(request, "profile.html")

@login_required
def add_bookmark(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    User_Recipe.objects.create(user=request.user, recipe=recipe)
    return redirect('recipe_detail', recipe_id=recipe_id)       #have to modifi



# def delete_url(request, id):
#     queryset = User.objects.get(id=id)
    # queryset.delete()
    # return redirect('/')

