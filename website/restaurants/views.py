from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Restaurant, Dishes, Chef

def index(request):
    return HttpResponse("hello world")

def index(request):
    restaurants = Restaurant.objects.all()
    context = {
        'page': 'where to eat romans food',
        'restaurants': restaurants
    }
    return render(request, 'restaurants/index.html', context)
