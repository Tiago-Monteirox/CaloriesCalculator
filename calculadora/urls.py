from django.urls import path
from . import views


urlpatterns = [
    path("list", views.list_food, name="list_food"),
    
]