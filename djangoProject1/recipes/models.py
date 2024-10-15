from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    instructions = models.TextField()
    # difficulty = models.PositiveSmallIntegerField(default=1,
                                                  # validators=[MinValueValidator(1), MaxValueValidator(10)])
    difficulty = models.IntegerField(choices=[(i, i) for i in range(1, 11)], default=1)
    # diff = models.TextChoices("")
