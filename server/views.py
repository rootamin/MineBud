from django.shortcuts import render, redirect
from django.contrib import messages


def adminsection(request):
    if request.user.is_superuser or request.user.groups.filter(name="Server Agent").exists() or request.user.groups.filter(name="Server Manager"):
        context = {}
        return render(request, "admin.html", context)

    else:
        messages.error(request, "You do not have permission to view this section.", extra_tags="alert alert-danger")
        return redirect("portal")
