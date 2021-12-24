from django.shortcuts import render
from .models import Dish, Category
from django.http  import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, decorators, mixins
import random, secrets

# Create your views here.

def index (request):
    return render(request, 'menu/index.html')

def category (request):
    categories = Category.objects.all()
    map = { 'categories': categories}
    return render(request, 'menu/category.html', map)

def dishByCategory(request, category_id):
    category = Category.objects.get(pk=category_id)
    dishes = Dish.objects.filter(category=category)
    map = { 'dishes': dishes}
    return render(request, 'menu/dishes.html', map)

def allDishes(request):
    dishes = Dish.objects.all()
    map = { 'dishes': dishes}
    return render(request, 'menu/dishes.html', map)

class DishDetail(View):
    def get(self, request, dish_id):
        dish = Dish.objects.get(pk=dish_id)
        map = { 'dish': dish}
        return render(request, 'menu/dish_detail.html', map)

def submit(request):
    id = request.POST['currentTimeStamp']
    # dish_id = random.randint(1, 6)
    # dish = Dish.objects.get(pk=dish_id)
    allDishes = Dish.objects.all()
    map = { 'dish': secrets.choice(allDishes)}
    return render(request, 'menu/index.html', map)

class Login(View):
    def get(self, request):
        return render(request, 'menu/login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        login = authenticate(username=username, password=password)
        if login is None:
            return HttpResponse('Failed')
        return HttpResponse('Pass')

@decorators.login_required(login_url='/login/')
def updateDish(request, dish_id):
    return HttpResponse("OK")
