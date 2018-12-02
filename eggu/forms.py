from django import forms

from . import models


class IngredientForm(forms.ModelForm):
    class Meta:
        model = models.Ingredient
        fields = [
            "title",
            "description",
            "order",
            "image",
        ]

