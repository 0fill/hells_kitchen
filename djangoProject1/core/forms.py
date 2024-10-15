from django import forms
from .models import User_Recipe

class User_RecipeForm(forms.ModelForm):
    class Meta:
        model = User_Recipe
        fields = ['recipe']