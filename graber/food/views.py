from django.shortcuts import render
from food.models import Recipe, Taste


def index(request):
    recipes = Recipe.objects.order_by('created_at')
    resposne = {'recipes': recipes}
    return render(request, 'food/index.html', context=resposne)


def detail(request):
    resposne = {'details': 'I am detail page'}
    return render(request, 'food/detail.html', context=resposne)


def taste(request):
    tastes = Taste.objects.order_by('created_at')
    response = {'tastes': tastes}
    return render(request, 'food/taste.html', context=response)
