import  arcade

class SoundManager:

    def __init__(self):

        self.shoot_sound= arcade.load_sound("assets/sound/shoot.wav")

    def play_shoot(self):

        arcade.play_sound(self.shoot_sound)
