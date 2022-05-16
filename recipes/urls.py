from django.urls import path

from . import views  # from recipes.views import home

urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe),
]
