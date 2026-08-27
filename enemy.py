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

    def draw_health_bar(self):
        health_width=40
        health_height=10

        health_ratio=self.health/self.max_health

        current_health_width = health_width * health_ratio

        # Background
        arcade.draw_rect_filled(
            arcade.rect.XYWH(
                self.center_x,
                self.center_y+35,
                health_width,
                health_height),
            arcade.color.DARK_RED
        )

        # Current health
        arcade.draw_rect_filled(
            arcade.rect.XYWH(
                self.center_x,
                self.center_y+35,
                current_health_width,
                health_height
            ),
            arcade.color.GREEN
        )
