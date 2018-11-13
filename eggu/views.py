from django.shortcuts import render

from .models import Sandwich, Ingredient


def home_egg(request):
    sandwich = Sandwich.objects.get(pk=1)
    return render(request, "eggu/home_egg.html", {"sandwich": sandwich})


def ingredient_detail(request, pk):
    ingredient = Ingredient.objects.get(pk=pk)
    return render(request, "eggu/ingredient_detail.html", {"ingredient": ingredient})
