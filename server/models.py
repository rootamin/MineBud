from django.db import models

# Create your models here.
class ServerProperties(models.Model):
    BOOLEAN_CHOICES = [
        ("True", "true"),
        ("False", "false")
    ]
    DIFFICULTY_CHOICES = [
        ("Peaceful", "peaceful"),
        ("Easy", "easy"),
        ("Normal", "normal"),
        ("Hard", "hard")
    ]
    OP_CHOICES = [
        ("0-All permissions", "0"),
        ("1-Moderator", "1"),
        ("2-Game Master", "2"),
        ("3-Admin", "3"),
        ("4-Owner", "4")
    ]
    gamemode = models.CharField(max_length=15, default="survival")
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default="Easy")
    max_players = models.IntegerField(default=20)
    white_list = models.CharField(max_length=5, choices=BOOLEAN_CHOICES, default="False")
    view_distance = models.IntegerField(default=10)
    simulation_distance = models.IntegerField(default=10)
    motd = models.CharField(max_length=59, default="A Minecraft Server", blank=True)
    hardcore = models.CharField(max_length=5, choices=BOOLEAN_CHOICES, default="False")
    online_mode = models.CharField(max_length=5, choices=BOOLEAN_CHOICES, default="True")
    pvp = models.CharField(max_length=5, choices=BOOLEAN_CHOICES, default="True")
    enable_command_block = models.CharField(max_length=5, choices=BOOLEAN_CHOICES, default="False")
    generator_settings = models.CharField(max_length=300, defualt="{}")
    enforce_secure_profile = models.CharField(max_length=5, choices=BOOLEAN_CHOICES, default="True")
    generate_structures = models.CharField(max_length=5, choices=BOOLEAN_CHOICES, default="true")
    max_chained_neighbour_updates = models.IntegerField(default=1000000)
    allow_nether = models.CharField(max_length=5, choices=BOOLEAN_CHOICES, default="True")
    op_permission_level = models.CharField(max_length=10, choices=OP_CHOICES, default="4-Owner")
    player_idle_timeout = models.IntegerField(default=0)
    spawn_npcs = models.CharField(max_length=5, choices=BOOLEAN_CHOICES, default="True")
    spawn_animals = models.CharField(max_length=5, choices=BOOLEAN_CHOICES, default="True")
    spawn_monsters = models.CharField(max_length=5, choices=BOOLEAN_CHOICES, default="True")
    spawn_protection = models.IntegerField(default=16)
    max_world_size = models.CharField(max_length=30, default="29999984")


