from django.urls import path

from . import views  # from recipes.views import home

app_name = 'recipes'

urlpatterns = [
    path('', views.RecipeListViewBase.as_view(), name="home"),
    path('recipes/search/', views.search, name="search"),
    path('recipes/category/<str:category_name>/',
         views.category, name="category"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),

]
