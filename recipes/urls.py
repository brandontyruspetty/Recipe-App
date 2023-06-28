from django.urls import path
from .views import welcome, RecipeListView, RecipeDetailView, records

app_name = 'recipes'

urlpatterns = [
    path('', welcome, name='home'),
    path('list/', RecipeListView.as_view(), name='list'),
    path('list/<pk>', RecipeDetailView.as_view(), name='detail'),
    path('search/', records, name='search'),
]
