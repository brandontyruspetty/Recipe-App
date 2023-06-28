from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import RecipeSearchForm
import pandas as pd
from .utils import get_recipename_from_id, get_chart

# Create your views here.


def welcome(request):
    return render(request, 'recipes/recipes_home.html')


class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes/recipes_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipes/detail.html'


@login_required
def records(request):
    form = RecipeSearchForm(request.POST or None)
    recipe_df = None
    recipe_difficulty = None
    chart = None
    qs = None

    if request.method == 'POST':
        recipe_difficulty = request.POST.get('recipe_difficulty')
        chart_type = request.POST.get('chart_type')

        if recipe_difficulty == 'easy':
            recipe_difficulty == 'Easy'
        if recipe_difficulty == 'medium':
            recipe_difficulty == 'Medium'
        if recipe_difficulty == 'intermediate':
            recipe_difficulty == 'Intermediate'
        if recipe_difficulty == 'hard':
            recipe_difficulty == 'Hard'

        qs = Recipe.objects.all()
        id_searched = []
        for obj in qs:
            difficulty = obj.calculate_difficulty()
            if difficulty == recipe_difficulty:
                id_searched.append(obj.id)

        qs = qs.filter(id__in=id_searched)

        if qs:
            recipe_df = pd.DataFrame(qs.values())
            chart = get_chart(chart_type, recipe_df,
                              labels=recipe_df['name'].values)

            recipe_df = recipe_df.to_html()

    context = {
        'form': form,
        'recipe_df': recipe_df,
        'recipe_difficulty': recipe_difficulty,
        'chart': chart,
        'qs': qs
    }

    return render(request, 'recipes/search.html', context)
