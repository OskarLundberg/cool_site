from django.urls import path

from . import views

app_name = "eggu"

urlpatterns = [
    path("", views.home_egg, name="home"),
    path("<int:pk>/", views.ingredient_detail, name="detail"),
    path("Community_sandwich/create_ingredient", views.create_ingredient, name="create_ingredient"),
    path("Community_sandwich/edit_ingredient/<int:ingredient_pk>", views.edit_ingredient, name="edit_ingredient"),
    path("Community_sandwich", views.community_sandwich, name="community_sandwich"),
]
    #path("<int:course_pk>/<int:step_pk>/", views.step_detail,
    #     name="step"),
    #path("<int:pk>/", views.course_detail, name="detail"),