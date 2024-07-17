from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from .forms import BrandForm
from .models import BrandModel

# Create your views here.


@method_decorator(login_required, name="dispatch")
class add_brand(CreateView):
    model = BrandModel
    form_class = BrandForm
    template_name = "add_brand.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
