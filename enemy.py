import arcade
import random
from settings import ENEMY_SPEED,ENEMY_HEALTH

class Enemy(arcade.Sprite):

    def __init__(self):
        super().__init__("assets/image/enemy.png")

        self.scale = 0.2
        self.speed = ENEMY_SPEED

        self.max_health = ENEMY_HEALTH
        self.health = self.max_health

        self.center_x = random.randint(50, 750)
        self.center_y = random.randint(400, 550)