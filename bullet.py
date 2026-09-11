import arcade
from settings import BULLET_SPEED, BULLET_SCALE, BULLET_DAMAGE

class Bullet(arcade.Sprite):

    def __init__(self, x, y):
        super().__init__("assets/image/bullet.png")

        self.scale = BULLET_SCALE
        self.speed = BULLET_SPEED

        self.center_x = x
        self.bottom = y

        self.damage = BULLET_DAMAGE