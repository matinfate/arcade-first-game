import arcade


class Bullet(arcade.Sprite):

    def __init__(self, x, y):
        super().__init__("assets/image/bullet.png")

        self.scale = 0.2
        self.speed = 500

        self.center_x = x
        self.bottom = y