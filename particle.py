import arcade
import random

from settings import (
    PARTICLE_MIN_SPEED,
    PARTICLE_MAX_SPEED,
    PARTICLE_LIFETIME,
    PARTICLE_SHRINK_SPEED
)

class Particle:

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.size = random.randint(3, 6)

        self.change_x = random.uniform(
            PARTICLE_MIN_SPEED,
            PARTICLE_MAX_SPEED
        )
        self.change_y = random.uniform(
            PARTICLE_MIN_SPEED,
            PARTICLE_MAX_SPEED
        )

        self.lifetime =  PARTICLE_LIFETIME
        self.timer = 0

    def update(self,delta_time):
        self.timer += delta_time

        self.x+=self.change_x*delta_time
        self.y+=self.change_y*delta_time

        self.size - PARTICLE_SHRINK_SPEED * delta_time
        
        return self.timer>=self.lifetime

    def draw(self):
        # Calculate transparency
        alpha = int(255 * (1 - self.timer / self.lifetime))

        # Create particale
        arcade.draw_circle_filled(
            self.x,
            self.y,
            self.size,
            (255, 165, 0, alpha)
        )
