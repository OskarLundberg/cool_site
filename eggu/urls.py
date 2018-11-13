from django.urls import path

from . import views

app_name = "eggu"

urlpatterns = [
    path("", views.home_egg, name="home"),
    path("<int:pk>/", views.ingredient_detail, name="detail"),
]
    #path("<int:course_pk>/<int:step_pk>/", views.step_detail,
    #     name="step"),
    #path("<int:pk>/", views.course_detail, name="detail"),