import  arcade

class SoundManager:

    def __init__(self):

        self.shoot_sound= arcade.load_sound("assets/sound/shoot.wav")
        self.enemy_death_sound= arcade.load_sound("assets/sound/enemy_death.wav")

    def play_shoot(self):

        arcade.play_sound(self.shoot_sound)

    def play_enemy_death(self):

        arcade.play_sound(self.enemy_death_sound)