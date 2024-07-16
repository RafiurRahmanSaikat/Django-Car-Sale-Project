from django.urls import path

from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.UserLogin.as_view(), name="login"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.UserLogout.as_view(), name="logout"),
    path("change_pass/", views.change_password, name="change_pass"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("forget_password/", views.forget_password, name="forget_password"),
]
