import arcade
import random


class Enemy(arcade.Sprite):

    def __init__(self):
        super().__init__("assets/image/enemy.png")

        self.scale = 0.2
        self.speed = 50

        self.center_x = random.randint(50, 750)
        self.center_y = random.randint(400, 550)