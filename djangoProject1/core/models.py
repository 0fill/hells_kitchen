from django.contrib.auth.models import User
from django.db import models

from recipes.models import Recipe


# Create your models here.

class User_Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
