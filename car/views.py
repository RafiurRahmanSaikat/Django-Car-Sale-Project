from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView

from .forms import CarForm, CommentForm
from .models import CarModel

# Create your views here.


@method_decorator(login_required, name="dispatch")
class add_car(CreateView):
    model = CarModel
    form_class = CarForm
    template_name = "add_car.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class car_details(DetailView):
    model = CarModel
    template_name = "car_details.html"
    pk_url_kwarg = "id"
    context_object_name = "car"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = self.object
            comment.save()
        return redirect("car_details", id=self.object.id)
