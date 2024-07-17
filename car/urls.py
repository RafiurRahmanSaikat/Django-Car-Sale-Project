from django.urls import path

from . import views

urlpatterns = [
    path("add/", views.add_car.as_view(), name="add_car"),
    path("details/<int:id>", views.car_details.as_view(), name="car_details"),
]
