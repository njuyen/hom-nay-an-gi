from django.shortcuts import render
from .models import Dish, Category

# Create your views here.

def index (request):
    dishes = ['bún bò', 'phở', 'hủ tiếu']
    map = { 'dishes': dishes}
    return render(request, "menu/index.html", map)

def category (request):
    categories = Category.objects.all()
    map = { 'categories': categories}
    return render(request, "menu/category.html", map)

def dishByCategory(request, category_id):
    category = Category.objects.get(pk=category_id)
    dishes = Dish.objects.filter(category=category)
    map = { 'dishes': dishes}
    return render(request, "menu/dishes.html", map)
