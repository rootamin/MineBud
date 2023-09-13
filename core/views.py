from django.shortcuts import render
from .models import Events


def index(request):
    events = Events.objects.all()

    context = {"events": events}
    return render(request, "index.html", context)
