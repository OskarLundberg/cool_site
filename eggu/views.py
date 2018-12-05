from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Sandwich, Ingredient
from . import forms


def home_egg(request):
    sandwich = Sandwich.objects.get(pk=1)
    return render(request, "eggu/home_egg.html", {"sandwich": sandwich})


def ingredient_detail(request, pk):
    ingredient = Ingredient.objects.get(pk=pk)
    c_sandwich = get_object_or_404(Sandwich, pk=2)
    return render(request, "eggu/ingredient_detail.html", {
        "ingredient": ingredient,
        "c_sandwich": c_sandwich})


def community_sandwich(request):
    sandwich = Sandwich.objects.get(pk=2)
    return render(request, "eggu/community_sandwich.html", {"sandwich": sandwich})


@login_required
def create_ingredient(request):
    """Lets a logged in user to create a new ingredient to the Community Sandwich"""
    form = forms.IngredientForm()
    sandwich = get_object_or_404(Sandwich, pk=2)

    # https://docs.djangoproject.com/en/2.1/topics/security/#user-uploaded-content-security
    if request.method == "POST":
        form = forms.IngredientForm(request.POST, request.FILES)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.Sandwich = sandwich
            ingredient.save()
            return HttpResponseRedirect(reverse("eggu:community_sandwich"))

    return render(request, "eggu/ingredient_form.html", {"form": form})


@login_required
def edit_ingredient(request, ingredient_pk):
    """lets a logged in user to edit the ingredients in the Community Sandwich"""
    # Still need to make it so the image gets deleted if the ingredient gets deleted
    # or if the image just gets changed (in editing)
    ingredient = get_object_or_404(Ingredient, pk=ingredient_pk)
    form = forms.IngredientForm(instance=ingredient)

    if request.method == "POST":
        form = forms.IngredientForm(request.POST, request.FILES, instance=ingredient)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("eggu:community_sandwich"))

    return render(request, "eggu/ingredient_form.html", {"form": form})

