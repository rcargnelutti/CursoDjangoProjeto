from django.http import Http404
from django.shortcuts import render
from utils.recipes.factory import make_recipe

from recipes.models import Recipe


def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        # 'recipes': [make_recipe() for _ in range(10)],
        'recipes': recipes,
    })


def category(request, category_name):
    recipes = Recipe.objects.filter(
        category__name=category_name,
        is_published=True,
    ).order_by('-id')

    if not recipes:
        raise Http404('Not found')

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes.first().category.name} - Category | '
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
