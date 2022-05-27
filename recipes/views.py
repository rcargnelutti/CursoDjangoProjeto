from django.http import Http404
from django.shortcuts import get_list_or_404, render
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
    # Exemplo com query set
    # recipes = Recipe.objects.filter(
    #     category__name=category_name,
    #     is_published=True,
    # ).order_by('-id')

    # if not recipes:
    #     raise Http404('Not found')

    # Exemplo com lista
    # recipes = get_list_or_404(
    #    Recipe, category__name=category_name, is_published=True)

    # exemplo com lista e query set
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__name=category_name,
            is_published=True,
        ).order_by('-id')
    )

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category | '
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
