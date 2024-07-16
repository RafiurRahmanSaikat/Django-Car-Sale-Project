from django.contrib.auth.models import User

# Create your models here.
from django.db import models

from brand.models import BrandModel


class CarModel(models.Model):
    brand = models.ForeignKey(
        BrandModel, on_delete=models.CASCADE, related_name="carbrand"
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to="cars/")

    def __str__(self):
        return self.title


class CommentModel(models.Model):
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.car.title}"
