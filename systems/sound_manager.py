import  arcade
from config.paths import resource_path

class SoundManager:

    def __init__(self):
        self.music_volume = 1
        self.volume = 0.5

        self. background_music=arcade.load_sound(resource_path("assets/sound/background_music.ogg"))
        self.background_music_player = None

        self.shoot_sound= arcade.load_sound(resource_path("assets/sound/shoot.wav"))
        self.enemy_death_sound= arcade.load_sound(resource_path("assets/sound/enemy_death.wav"))
        self.power_up_sound= arcade.load_sound(resource_path("assets/sound/power_up.wav"))
        self.player_hit_sound= arcade.load_sound(resource_path("assets/sound/player_hit.wav"))
        self.wave_start_sound= arcade.load_sound(resource_path("assets/sound/wave_start.wav"))
        self.game_over_sound= arcade.load_sound(resource_path("assets/sound/game_over.wav"))

    def play_background_music(self):
        self.background_music_player = self.background_music.play(volume=self.music_volume,loop=True)

    def stop_background_music(self):
        if self.background_music_player:
            self.background_music_player.pause()
            self.background_music_player = None

    def play_shoot(self):
        arcade.play_sound(self.shoot_sound,volume=self.volume)

    def play_enemy_death(self):
        arcade.play_sound(self.enemy_death_sound,volume=self.volume)

    def play_power_up(self):
        arcade.play_sound(self.power_up_sound,volume=self.volume)

    def play_player_hit(self):
        arcade.play_sound(self.player_hit_sound,volume=self.volume)

    def play_wave_start(self):
        arcade.play_sound(self.wave_start_sound,volume=self.volume)

    def play_game_over(self):
        arcade.play_sound(self.game_over_sound,volume=self.volume)


