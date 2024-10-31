from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'ingredients', 'instructions', 'difficulty']


class RecipeSearchForm(forms.Form):
    recipe_name = forms.CharField(required=False, label='Recipe Name')
    RECIPE_DIFFICULTY_CHOICES = [('', 'None')] + [(str(i), str(i)) for i in range(1, 11)]
    recipe_difficulty = forms.ChoiceField(
        choices=RECIPE_DIFFICULTY_CHOICES,
        label='Recipe Difficulty',
        required=False
    )

    def clean_recipe_difficulty(self):
        data = self.cleaned_data['recipe_difficulty']
        if data == "":
            return None
        return data
