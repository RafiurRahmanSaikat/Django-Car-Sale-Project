from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from car.models import CarModel

from .models import OrderModel

# Create your views here.


@login_required
def order(request, car_id):
    car = CarModel.objects.get(id=car_id)
    if car.quantity > 0:
        car.quantity -= 1
        car.save()
        OrderModel.objects.create(user=request.user, car=car)
    else:
        return redirect("profile")

    return redirect("profile")
