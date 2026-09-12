import arcade
import random

from settings import (
    ENEMY_SPEED,
    ENEMY_HEALTH,
    ENEMY_SCORE,
    ENEMY_DAMAGE,
    FAST_ENEMY_SPEED,
    FAST_ENEMY_HEALTH,
    FAST_ENEMY_SCORE,
    FAST_ENEMY_DAMAGE,
    FAST_ENEMY_ZIGZAG_SPEED,
    FAST_ENEMY_ZIGZAG_INTERVAL,
    TANK_ENEMY_SPEED,
    TANK_ENEMY_HEALTH,
    TANK_ENEMY_SCORE,
    TANK_ENEMY_DAMAGE,
    TANK_ENEMY_KNOCKBACK
)

class Enemy(arcade.Sprite):

    def __init__(self, image="assets/image/enemy.png"):
        super().__init__(image)

        self.scale = 0.2
        self.speed = ENEMY_SPEED

        self.score = ENEMY_SCORE

        self.max_health = ENEMY_HEALTH
        self.health = self.max_health

        self.damage = ENEMY_DAMAGE

        self.center_x = random.randint(50, 750)
        self.center_y = random.randint(400, 550)

    def move_toward_player(self,player,delta_time):

        if self.center_x < player.center_x:
            self.center_x += self.speed*delta_time
        elif self.center_x > player.center_x:
            self.center_x -= self.speed*delta_time

        if self.center_y < player.center_y:
            self.center_y += self.speed * delta_time
        elif self.center_y > player.center_y:
            self.center_y -= self.speed * delta_time

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

    def avoid_enemy(self,other,delta_time):
        if arcade.check_for_collision(self, other):
            if self.center_x < other.center_x:
                self.center_x -= self.speed*delta_time
            elif self.center_x > other.center_x:
                self.center_x += self.speed*delta_time

            if self.center_y < other.center_y:
                self.center_y -= self.speed*delta_time
            elif self.center_y > other.center_y:
                self.center_y += self.speed*delta_time

class FastEnemy(Enemy):

    def __init__(self):
        super().__init__("assets/image/fast_enemy.png")

        self.scale = 0.1
        self.speed = FAST_ENEMY_SPEED
        self.max_health = FAST_ENEMY_HEALTH
        self.health = self.max_health
        self.score = FAST_ENEMY_SCORE
        self.damage = FAST_ENEMY_DAMAGE

        self.zigzag_timer = 0
        self.zigzag_direction = 1

    def move_toward_player(self, player, delta_time):
        # Move toward the player
        super().move_toward_player(player, delta_time)

        # Update zigzag timer
        self.zigzag_timer += delta_time

        # Change direction every 0.4 seconds
        if self.zigzag_timer >= FAST_ENEMY_ZIGZAG_INTERVAL:
            self.zigzag_timer = 0
            self.zigzag_direction *= -1

        # Add horizontal zigzag movement
        self.center_x += (FAST_ENEMY_ZIGZAG_SPEED * self.zigzag_direction * delta_time)

class TankEnemy(Enemy):

    def __init__(self):
        super().__init__("assets/image/tank_enemy.png")

        self.scale = 0.5
        self.speed = TANK_ENEMY_SPEED
        self.max_health = TANK_ENEMY_HEALTH
        self.health = self.max_health
        self.score = TANK_ENEMY_SCORE
        self.damage = TANK_ENEMY_DAMAGE

        self.knockback = TANK_ENEMY_KNOCKBACK