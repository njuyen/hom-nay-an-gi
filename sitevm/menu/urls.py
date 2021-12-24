from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('category/', views.category, name='category'),
    path('category/<int:category_id>', views.dishByCategory, name='dishByCategory'),
    path('dish/', views.allDishes, name='allDishes'),
    path('dish/<int:dish_id>', views.DishDetail.as_view(), name='dishDetail'),
    path('dish/<int:dish_id>/update', views.updateDish, name='dishUpdate'),
    path('login/', views.Login.as_view(), name='login'),
    path('submit/', views.submit, name='submit')
]
