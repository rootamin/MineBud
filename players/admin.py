from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import AdminPasswordChangeForm
from .models import Player


class PlayerAdmin(UserAdmin):
    change_password_form = AdminPasswordChangeForm


admin.site.register(Player, PlayerAdmin)
