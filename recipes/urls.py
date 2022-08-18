from django.urls import path

from . import views  # from recipes.views import home

app_name = 'recipes'

urlpatterns = [
    path('',
         views.RecipeListViewHome.as_view(),
         name="home"
         ),
    path('recipes/search/',
         views.RecipeListViewSearch.as_view(),
         name="search"
         ),
    path('recipes/category/<int:category_id>/',
         views.RecipeListViewCategory.as_view(),
         name="category"
         ),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(),
         name="recipe"
         ),

    # Api

    path('recipes/api/v1/',
         views.RecipeListViewHomeApi.as_view(),
         name="home_api"
         ),
    path('recipes/api/v1/<int:pk>/',
         views.RecipeDetailApi.as_view(),
         name="home_api_detail"
         ),
]
