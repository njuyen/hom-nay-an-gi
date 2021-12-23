from django.contrib import admin
from .models import Category, Dish

# Register your models here.
admin.site.Register(Category)
admin.site.Register(Dish)
