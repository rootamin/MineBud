from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ServerProperties
from .forms import ServerPropertiesForm

from django.http import JsonResponse
import subprocess
import os
import signal
from .minecraft import process


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


def start_server(request):
    global process
    # Command to start the Minecraft server
    command = "java -Xmx1024M -Xms1024M -jar fabric.jar nogui"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE, cwd="minecraft")
    return JsonResponse({'status': 'Server started'})


def stop_server(request):
    global process
    if process:
        os.kill(process.pid, signal.SIGTERM)
        process = None
        return JsonResponse({'status': 'Server stopped'})
    else:
        return JsonResponse({'status': 'Server not running'})