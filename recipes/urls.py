from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from recipes import views

app_name = 'recipes'

recipe_api_v2_router = SimpleRouter()
recipe_api_v2_router.register(
    'recipes/api/v2',
    views.RecipeAPIv2ViewSet,
    basename='recipes-api',
)

urlpatterns = [
    path('',
         views.RecipeListViewHome.as_view(),
         name="home"
         ),
    path('recipes/search/',
         views.RecipeListViewSearch.as_view(),
         name="search"
         ),
    path('recipes/tags/<slug:slug>/',
         views.RecipeListViewTag.as_view(),
         name="tag"
         ),
    path('recipes/category/<int:category_id>/',
         views.RecipeListViewCategory.as_view(),
         name="category"
         ),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(),
         name="recipe"
         ),

    path('recipes/theory/',
         views.theory,
         name="theory"
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
     path(
        'recipes/api/v2/tag/<int:pk>/',
        views.tag_api_detail,
        name='recipes_api_v2_tag',
        ),
     path(
          'recipes/api/token/', 
          TokenObtainPairView.as_view(), 
          name='token_obtain_pair'
          ),
     path(
          'recipes/api/token/refresh/', 
          TokenRefreshView.as_view(), 
          name='token_refresh'
          ),
     path(
          'recipes/api/token/verify/', 
          TokenVerifyView.as_view(), 
          name='token_verify'
          ),
     # por último
     path('', include(recipe_api_v2_router.urls)),
]
