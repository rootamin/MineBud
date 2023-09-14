from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import RegistrationForm, ProfileForm
from .models import Player


@login_required(login_url="login")
def portal(request):
    player = request.user

    try:
        player_profile = Player.objects.get(username=player)
    except Player.DoesNotExist:
        messages.error(request, "Invalid User", extra_tags="alert alert-danger")
        return redirect("home")

    if request.method == "POST":
        profile_form = ProfileForm(request.POST, instance=player_profile)

        if profile_form.is_valid():
            profile_form.save()

            messages.success(request, "Saved Successfully", extra_tags="alert alert-success")
            return redirect('portal')

        else:
            messages.error(request, "Please fill the form correctly.", extra_tags="alert alert-warning")

    else:
        profile_form = ProfileForm(instance=player_profile)

    context = {"player_profile": player_profile, "profile_form": profile_form}

    return render(request, "portal.html", context)


def signin(request):
    if request.user.is_authenticated:
        player = Player.objects.get(username=request.user)
        messages.info(request, f"You are already logged in as {player.username}", extra_tags="alert alert-info")
        return redirect("home")

    else:

        if request.method == "POST":
            username = request.POST.get('username').lower()
            password = request.POST.get('password')

            try:
                user = Player.objects.get(username=username)
            except:
                messages.error(request, "User does not exist!", extra_tags='alert alert-warning')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                player = Player.objects.get(username=request.user)
                messages.success(request, f"Welcome {player.username}", extra_tags='alert alert-success')
                return redirect("portal")
            else:
                messages.error(request, "Invalid credentials.", extra_tags='alert alert-danger')

    return render(request, 'login.html')


def signout(request):
    if request.user.is_authenticated:
        player = Player.objects.get(username=request.user)
        logout(request)
        messages.success(request, f"You have successfully logged out from {player.username}.", extra_tags="alert alert-success")
        return redirect("home")
    else:
        messages.error(request, "You need to be authenticated in order to logout.", extra_tags='alert alert-warning')
        return redirect("home")


def signup(request):
    if request.user.is_authenticated:
        player = Player.objects.get(username=request.user)
        messages.info(request, f"You are already logged in as {player.username}", extra_tags="alert alert-info")
        return redirect("home")

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.username = user.username.lower()
            user.save()
            login(request, user)  # Automatically logs in the user after registration
            messages.success(request, f"Registration was successful {user.username}", extra_tags="alert alert-success")
            return redirect('home')
        else:
            messages.error(request, "An error occurred.", extra_tags="alert alert-danger")

    else:
        form = RegistrationForm()

    return render(request, "signup.html", {"form": form})

