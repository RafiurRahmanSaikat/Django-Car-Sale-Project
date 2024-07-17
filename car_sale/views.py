from django.shortcuts import get_object_or_404, render

from brand.models import BrandModel
from car.models import CarModel


def cars_by_brand(request, brand_id):
    brand = get_object_or_404(BrandModel, id=brand_id)
    cars = CarModel.objects.filter(brand=brand)
    context = {
        "brand": brand,
        "cars": cars,
    }
    return render(request, "cars/cars_by_brand.html", context)


# Create your views here.
def search_by_brand(request, id):
    brands = BrandModel.objects.all()
    brand = brands.get(id=id)
    cars = CarModel.objects.filter(brand=brand)
    return render(
        request, "home.html", {"car": cars, "brand": brands, "brand_name": brand}
    )


def home(request):
    cars = CarModel.objects.all()
    brands = BrandModel.objects.all()
    return render(request, "home.html", {"car": cars, "brand": brands})
