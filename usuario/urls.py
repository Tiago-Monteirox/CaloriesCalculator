from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
    path("", views.home, name="home"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
]