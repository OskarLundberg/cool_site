from django.db import models


class Sandwich(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="pics", blank=True)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)
    image = models.ImageField(upload_to="pics", blank=True)
    Sandwich = models.ForeignKey(Sandwich, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ["order", ]

    def __str__(self):
        return self.title
