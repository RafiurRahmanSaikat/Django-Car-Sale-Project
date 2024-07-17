from django.urls import path

from . import views

urlpatterns = [
    path("order/<int:car_id>", views.order, name="order"),
]
