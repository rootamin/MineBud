from django.db import models
from django.conf import settings
import os


class ServerProperties(models.Model):
    GAMEMODE_CHOICES = [
        ("survival", "Survival"),
        ("creative", "Creative"),
        ("adventure", "Adventure")
    ]
    BOOLEAN_CHOICES = [
        ("true", "True"),
        ("false", "False")
    ]
    DIFFICULTY_CHOICES = [
        ("peaceful", "Peaceful"),
        ("easy", "Easy"),
        ("normal", "Normal"),
        ("hard", "Hard")
    ]
    OP_CHOICES = [
        ("0", "0-All permissions"),
        ("1", "1-Moderator"),
        ("2", "2-Game Master"),
        ("3", "3-Admin"),
        ("4", "4-Owner")
    ]
    gamemode = models.CharField(max_length=15, choices=GAMEMODE_CHOICES, default="survival")
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default="easy")
    max_players = models.IntegerField(default=20)
    white_list = models.CharField(max_length=5, choices=BOOLEAN_CHOICES, default="false")
    view_distance = models.IntegerField(default=10)
    simulation_distance = models.IntegerField(default=10)
    motd = models.CharField(max_length=59, default="A Minecraft Server", blank=True)
    hardcore = models.CharField(max_length=5, choices=BOOLEAN_CHOICES, default="false")
    online_mode = models.CharField(max_length=5, choices=BOOLEAN_CHOICES, default="true")
    pvp = models.CharField(max_length=5, choices=BOOLEAN_CHOICES, default="true")
    enable_command_block = models.CharField(max_length=5, choices=BOOLEAN_CHOICES, default="false")
    generator_settings = models.CharField(max_length=300, default="{}")
    enforce_secure_profile = models.CharField(max_length=5, choices=BOOLEAN_CHOICES, default="true")
    generate_structures = models.CharField(max_length=5, choices=BOOLEAN_CHOICES, default="true")
    max_chained_neighbour_updates = models.IntegerField(default=1000000)
    allow_nether = models.CharField(max_length=5, choices=BOOLEAN_CHOICES, default="true")
    op_permission_level = models.CharField(max_length=20, choices=OP_CHOICES, default="4")
    player_idle_timeout = models.IntegerField(default=0)
    spawn_npcs = models.CharField(max_length=5, choices=BOOLEAN_CHOICES, default="true")
    spawn_animals = models.CharField(max_length=5, choices=BOOLEAN_CHOICES, default="true")
    spawn_monsters = models.CharField(max_length=5, choices=BOOLEAN_CHOICES, default="true")
    spawn_protection = models.IntegerField(default=16)
    max_world_size = models.CharField(max_length=30, default="29999984")
    level_seed = models.CharField(max_length=50, blank=True)
    level_type = models.CharField(max_length=30, default=r"minecraft\\:normal")

    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        file_path = os.path.join(settings.BASE_DIR, 'minecraft', 'server.properties')
        with open(file_path, 'w') as file:
            file.write(f'enable-jmx-monitoring=false\nrcon.port=25575\nlevel-seed={self.level_seed}\ngamemode={self.gamemode}\nenable-command-block={self.enable_command_block}\nenable-query=true\ngenerator-settings={self.generator_settings}\nenforce-secure-profile=true\nlevel-name=world\nmotd={self.motd}\nquery.port=25565\npvp={self.pvp}\ngenerate-structures={self.generate_structures}\nmax-chained-neighbor-updates={self.max_chained_neighbour_updates}\ndifficulty={self.difficulty}\nnetwork-compression-threshold=256\nmax-tick-time=60000\nrequire-resource-pack=false\nuse-native-transport=true\nmax-players={self.max_players}\nonline-mode={self.online_mode}\nenable-status=true\nallow-flight=false\ninitial-disabled-packs=\nbroadcast-rcon-to-ops=true\nview-distance={self.view_distance}\nserver-ip=\nresource-pack-prompt=\nallow-nether={self.allow_nether}\nserver-port=25565\nenable-rcon=false\nsync-chunk-writes=true\nop-permission-level={self.op_permission_level}\nprevent-proxy-connections=false\nhide-online-players=false\nresource-pack=\nentity-broadcast-range-percentage=100\nsimulation-distance={self.simulation_distance}\nrcon.password=\nplayer-idle-timeout={self.player_idle_timeout}\nforce-gamemode=false\nrate-limit=0\nhardcore={self.hardcore}\nwhite-list={self.white_list}\nbroadcast-console-to-ops=true\nspawn-npcs={self.spawn_npcs}\nspawn-animals={self.spawn_animals}\nfunction-permission-level=2\ninitial-enabled-packs=vanilla\nlevel-type={self.level_type}\ntext-filtering-config=\nspawn-monsters={self.spawn_monsters}\nenforce-whitelist=false\nspawn-protection={self.spawn_protection}\nresource-pack-sha1=\nmax-world-size={self.max_world_size}')


    def __str__(self):
        return f"Modified On {self.created}"
