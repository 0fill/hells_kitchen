from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'ingredients', 'instructions', 'difficulty']


class RecipeSearchForm(forms.Form):
    recipe_name = forms.CharField(label='Recipe name', max_length=100)
    recipe_difficulty = forms.ChoiceField(choices=range(10), label='Recipe difficulty')
