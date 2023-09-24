from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ServerProperties
from .forms import ServerPropertiesForm


def adminsection(request):
    if request.method == "POST":
        if request.user.is_superuser or request.user.groups.filter(name="Server Manager"):

            form = ServerPropertiesForm(request.POST)
            if form.is_valid():
                form.save()

                messages.success(request, "Successfully changed server properties.", extra_tags="alert alert-success")
                return redirect("admin")

            else:
                messages.error(request, "An error occurred", extra_tags="alert alert-danger")
                return redirect("admin")
        else:
            messages.error(request, "You do not have permission to edit server properties", extra_tags="alert alert-danger")
            return redirect("admin")

    else:
        if request.user.is_superuser or request.user.groups.filter(name="Server Agent").exists() or request.user.groups.filter(name="Server Manager"):
            last_server_properties = ServerProperties.objects.last()
            server_properties = ServerPropertiesForm(instance=last_server_properties)
            context = {'server_properties': server_properties}
            return render(request, "admin.html", context)

        else:
            messages.error(request, "You do not have permission to view this section.", extra_tags="alert alert-danger")
            return redirect("portal")
