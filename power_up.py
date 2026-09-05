import arcade

class HealthPowerUp(arcade.Sprite):

    def __init__(self):
        super().__init__("assets/image/health_powerup.png")

        self.scale = 0.02
        self.health_amount = 25
        self.speed = 80

    def fall(self,delta_time):
        self.center_y -= self.speed * delta_time