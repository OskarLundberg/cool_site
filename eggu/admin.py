from django.contrib import admin

from .models import Sandwich, Ingredient

#  finns TabularInline  |  StackedInline
class IngredientInline(admin.StackedInline):
    model = Ingredient


class SandwichAdmin(admin.ModelAdmin):
    inlines = [IngredientInline,]

# Register your models here.
admin.site.register(Sandwich, SandwichAdmin)
admin.site.register(Ingredient)