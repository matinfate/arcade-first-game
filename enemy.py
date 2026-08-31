import arcade
import random
from settings import ENEMY_SPEED,ENEMY_HEALTH

class Enemy(arcade.Sprite):

    def __init__(self, image="assets/image/enemy.png"):
        super().__init__(image)

        self.scale = 0.2
        self.speed = ENEMY_SPEED

        self.score = 10

        self.max_health = ENEMY_HEALTH
        self.health = self.max_health

        self.center_x = random.randint(50, 750)
        self.center_y = random.randint(400, 550)

    def draw_health_bar(self):
        health_width = 40
        health_height = 5

        health_ratio = self.health / self.max_health

        current_width = health_width * health_ratio

        arcade.draw_rect_filled(
            arcade.rect.XYWH(
                self.center_x,
                self.center_y + 30,
                health_width,
                health_height
            ),
            arcade.color.DARK_RED
        )

        arcade.draw_rect_filled(
            arcade.rect.XYWH(
                self.center_x - (health_width - current_width) / 2,
                self.center_y + 30,
                current_width,
                health_height),
            arcade.color.GREEN
        )

class FastEnemy(Enemy):

    def __init__(self):
        super().__init__("assets/image/fast_enemy.png")

        self.scale = 0.1
        self.speed=100
        self.max_health=20
        self.health=self.max_health
        self.score=20

class TankEnemy(Enemy):

    def __init__(self):
        super().__init__("assets/image/tank_enemy.png")

        self.scale = 0.5
        self.speed = 30
        self.max_health = 80
        self.health = self.max_health
        self.score=30