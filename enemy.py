import arcade
import random
from settings import ENEMY_SPEED

class Enemy(arcade.Sprite):

    def __init__(self):
        super().__init__("assets/image/enemy.png")

        self.scale = 0.2
        self.speed = ENEMY_SPEED

        self.center_x = random.randint(50, 750)
        self.center_y = random.randint(400, 550)