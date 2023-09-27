from django.urls import path
from . import views

urlpatterns = [
    path("", views.adminsection, name="admin"),

    path('start-server/', views.start_server, name="start_server"),
    path('stop-server/', views.stop_server, name="stop_server"),
]
