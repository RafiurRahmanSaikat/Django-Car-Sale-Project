from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("car/", include("car.urls")),
    path("brand/", include("brand.urls")),
    path("account/", include("account.urls")),
    path("order/", include("order.urls")),
]
