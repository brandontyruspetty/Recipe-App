from django.shortcuts import render
from .models import Recipe

# Create your views here.


def welcome(request):
    return render(request, 'recipes/recipes_home.html')
