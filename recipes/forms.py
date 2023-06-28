from django import forms

CHART__CHOICES = (
    ('#1', 'Bar chart'),
    ('#2', 'Pie chart'),
    ('#3', 'Line chart')
)

DIFFICULTY__CHOICES = (
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('intermediate', 'Intermediate'),
    ('hard', 'Hard')
)


class RecipeSearchForm(forms.Form):
    recipe_difficulty = forms.ChoiceField(choices=DIFFICULTY__CHOICES)
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)
