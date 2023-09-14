from django.urls import path
from . import views

urlpatterns = [
    path("", views.adminsection, name="admin"),
]
