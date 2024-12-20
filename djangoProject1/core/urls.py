from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', HomePage, name="not"),
    path('home/', HomePage, name="home"),
    path('about/', AboutPage, name="about"),
    path('contact/', ContactPage, name="contacts"),
    path('profile/', profile, name="profile"),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="home.html"), name="logout"),
    path('registration/', registration, name="registration"),
]