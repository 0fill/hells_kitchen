from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from .models import Recipe
from .forms import RecipeForm, RecipeSearchForm
from django.contrib.auth.mixins import LoginRequiredMixin
import os
from django.http import FileResponse, JsonResponse
from django.conf import settings


# Create your views here.

class RecipeListVeiw(ListView):
    model = Recipe
    template_name = 'recipe_list.html'
    context_object_name = 'page_obj'
    # paginate_by = 8


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_form.html'
    success_url = reverse_lazy('recipe_menu')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_form.html'
    success_url = reverse_lazy('recipe_menu')


class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = 'recipe_delete.html'
    success_url = reverse_lazy('recipe_menu')


def search_recipe(request):
    form = RecipeSearchForm()
    results = Recipe.objects.all()  # Initialize results early to avoid UnboundLocalError

    if request.method == 'POST':
        form = RecipeSearchForm(request.POST)
        if form.is_valid():
            recipe_name = form.cleaned_data.get('recipe_name', '')
            recipe_difficulty = form.cleaned_data.get('recipe_difficulty', None)

            if recipe_name:
                results = results.filter(name__icontains=recipe_name)

            if recipe_difficulty is not None and recipe_difficulty is not "":
                results = results.filter(difficulty__in=recipe_difficulty)

    return render(request, 'search_results.html', {'form': form, 'results': results})
