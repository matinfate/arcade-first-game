import arcade

from settings import PLAYER_HEALTH

class PowerUp(arcade.Sprite):

    def __init__(self, image, scale=0.02, speed=80):
        super().__init__(image)

        self.scale = scale
        self.speed = speed

    def fall(self, delta_time):
        self.center_y -= self.speed * delta_time

class HealthPowerUp(PowerUp):

    def __init__(self):
        super().__init__("assets/image/health_powerup.png")

        self.health_amount = 25

    def collect(self, player):
        player.health = min(
            PLAYER_HEALTH,
            player.health + self.health_amount
        )

class ShieldPowerUp(PowerUp):

    def __init__(self):
        super().__init__("assets/image/shield_powerup.png")

        self.duration = 5.0

    def collect(self, player):
        player.activate_shield(self.duration)

class RapidFirePowerUp(PowerUp):

    def __init__(self):
        super().__init__("assets/image/rapid_fire_powerup.png")

        self.duration = 5.0

    def collect(self, player):
        player.activate_rapid_fire(self.duration)