from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ServerProperties
from .forms import ServerPropertiesForm

from django.http import JsonResponse
from .minecraft import MinecraftServer


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


minecraft_server = MinecraftServer()

def start_server(request):
    if request.user.is_superuser or request.user.groups.filter(name="Server Manager"):
        if minecraft_server.process:
            messages.warning(request, "Server is already running. if you've stopped the server, use force stop button and start again.", extra_tags="alert alert-danger")
            return redirect("admin")
        else:
            minecraft_server.start()
            messages.success(request, "Server started.", extra_tags="alert alert-success")
            return redirect("admin")

    else:
        messages.error(request, "You do not have permission to start the server.", extra_tags="alert alert-danger")
        return redirect('admin')


def stop_server(request):
    if request.user.is_superuser or request.user.groups.filter(name="Server Manager"):
        if minecraft_server.process:
            minecraft_server.stop()
            messages.success(request, "Server stopped.", extra_tags="alert alert-success")
            return redirect("admin")
        else:
            messages.warning(request, "Server is not running. if there are any instances, just kill them.", extra_tags="alert alert-danger")
            return redirect("admin")
    else:
        messages.error(request, "You do not have permission to stop the server.", extra_tags="alert alert-danger")
        return redirect('admin')




