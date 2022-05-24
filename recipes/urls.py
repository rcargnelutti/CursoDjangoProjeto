from django.urls import path

from . import views  # from recipes.views import home

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),

    path('recipes/category/<str:category_name>/',
         views.category, name="category"),

    path('recipes/<int:id>/', views.recipe, name="recipe"),
]
