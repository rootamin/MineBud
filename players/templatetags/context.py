from players.models import Player


def profile_data(request):
    if request.user.is_authenticated:
        profile = Player.objects.get(username=request.user)
        player_username = profile.username
        profile_picture = profile.profile_pic
        context = {"player_username": player_username, "player_pic": profile_picture}

    else:
        context = ''

    return context
