import  arcade

class SoundManager:

    def __init__(self):
        self.shoot_sound= arcade.load_sound("assets/sound/shoot.wav")
        self.enemy_death_sound= arcade.load_sound("assets/sound/enemy_death.wav")
        self.power_up_sound= arcade.load_sound("assets/sound/power_up.wav")
        self.player_hit_sound= arcade.load_sound("assets/sound/player_hit.wav")
        self.wave_start_sound= arcade.load_sound("assets/sound/wave_start.wav")
        self.game_over_sound= arcade.load_sound("assets/sound/game_over.wav")

    def play_shoot(self):
        arcade.play_sound(self.shoot_sound)

    def play_enemy_death(self):
        arcade.play_sound(self.enemy_death_sound)

    def play_power_up(self):
        arcade.play_sound(self.power_up_sound)

    def play_player_hit(self):
        arcade.play_sound(self.player_hit_sound)

    def play_wave_start(self):
        arcade.play_sound(self.wave_start_sound)

    def play_game_over(self):
        arcade.play_sound(self.game_over_sound)