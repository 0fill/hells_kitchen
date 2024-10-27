from django.urls import path, re_path
from django.views.generic import ListView, DetailView
from .views import *

urlpatterns = [
    path("",
         RecipeListVeiw.as_view(),
         name='recipe_menu'),
    path("food/<int:pk>/",
         DetailView.as_view(template_name="recipe_detail.html",
                            model=Recipe),
                             name="recipe_detail"),
    path("create/", RecipeCreateView.as_view(), name="recipe_create"),
    path("update/<int:pk>/", RecipeUpdateView.as_view(), name="recipe_update"),
    path("delete/<int:pk>/", RecipeDeleteView.as_view(), name="recipe_delete"),
    path('search/', search_recipe, name='search'),
]
