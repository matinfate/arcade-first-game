import arcade

from config.settings import PLAYER_HEALTH,SHIELD_DURATION, RAPID_FIRE_DURATION

HEALTH_POWERUP_TEXTURE = arcade.load_texture(
    "assets/image/health_powerup.png"
)

SHIELD_POWERUP_TEXTURE = arcade.load_texture(
    "assets/image/shield_powerup.png"
)

RAPID_FIRE_POWERUP_TEXTURE = arcade.load_texture(
    "assets/image/rapid_fire_powerup.png"
)

class PowerUp(arcade.Sprite):

    def __init__(self, image, scale=0.02, speed=80):
        super().__init__(image)

        self.scale = scale
        self.speed = speed

    def fall(self, delta_time):
        self.center_y -= self.speed * delta_time

class HealthPowerUp(PowerUp):

    def __init__(self):
        super().__init__(HEALTH_POWERUP_TEXTURE)

        self.health_amount = 25

    def collect(self, player):
        player.health = min(
            PLAYER_HEALTH,
            player.health + self.health_amount
        )

class ShieldPowerUp(PowerUp):

    def __init__(self):
        super().__init__(SHIELD_POWERUP_TEXTURE)

        self.duration = SHIELD_DURATION

    def collect(self, player):
        player.activate_shield(self.duration)

class RapidFirePowerUp(PowerUp):

    def __init__(self):
        super().__init__(RAPID_FIRE_POWERUP_TEXTURE)

        self.duration = RAPID_FIRE_DURATION

    def collect(self, player):
        player.activate_rapid_fire(self.duration)