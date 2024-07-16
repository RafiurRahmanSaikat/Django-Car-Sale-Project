from django.shortcuts import render

from brand.models import BrandModel
from car.models import CarModel

# Create your views here.


def home(request):
    cars = CarModel.objects.all()
    brands = BrandModel.objects.all()
    print("Car", cars, "brands", brands)

    return render(request, "home.html", {"car": cars, "brand": brands})
