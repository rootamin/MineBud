from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.portal, name="portal"),

    path("login/", views.signin, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.signout, name="logout"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
