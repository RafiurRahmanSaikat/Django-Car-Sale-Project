from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, RedirectView, UpdateView

from .forms import EditUserForm, RegisterForm


# Create your views here.
def home(request):
    return render(request, "home.html")


class UserLogin(LoginView):
    template_name = "register.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Login"
        return context

    def form_valid(self, form):
        messages.success(self.request, "Login successful")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid credentials")
        return super().form_invalid(form)

    def get_success_url(self) -> str:
        return reverse_lazy("home")


class UserLogout(RedirectView):
    url = reverse_lazy("home")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


def profile(request):
    if request.user.is_authenticated:
        return render(request, "profile.html", {"user": request.user})
    else:
        return redirect("login")


def signup(request):
    if request.user.is_authenticated:
        return redirect("profile")
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, "Account created successfully")
            form.save(commit=True)
            print(form.cleaned_data)

            return redirect("profile")

    else:
        form = RegisterForm()

    return render(request, "signup.html", {"form": form})


def change_password(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password Changed Successfully")
            return redirect("profile")
    else:
        messages.error(request, "Password Change Failed")
        form = PasswordChangeForm(user=request.user)
    return render(request, "change_password.html", {"form": form})


def forget_password(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method == "POST":
        form = SetPasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password Changed Successfully")
            return redirect("profile")
    else:

        form = SetPasswordForm(user=request.user)
    return render(request, "change_password.html", {"form": form})


def edit_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = EditUserForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                print("Edit Profile", form.cleaned_data)
                messages.success(request, "Profile Updated Successfully")
                return redirect("profile")
        else:

            form = EditUserForm(instance=request.user)
        return render(request, "edit_profile.html", {"form": form})
