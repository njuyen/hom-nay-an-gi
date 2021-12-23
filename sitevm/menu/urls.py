from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('category/', views.category, name='category'),
    path('category/<int:category_id>', views.dishByCategory, name='dishes')
]
