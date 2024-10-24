from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django import forms
import json


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.CharField(max_length=1024)
    instructions = models.TextField()
    difficulty = models.IntegerField(choices=[(i, i) for i in range(1, 11)], default=1)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # diff = models.TextChoices("")



