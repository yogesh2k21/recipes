from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe/create/', views.create_recipe, name='create_recipe'),
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/edit/<int:recipe_id>/', views.edit_recipe, name='edit_recipe'),
    path('recipe/search/', views.search, name='search'),
]
  