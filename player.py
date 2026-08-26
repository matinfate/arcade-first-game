import arcade

from settings import (
    PLAYER_SPEED,
    PLAYER_HEALTH,
    PLAYER_DAMAGE,
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)

class Player(arcade.Sprite):

    def __init__(self):

        # Create a Sprite using the player image.
        super().__init__("assets/image/player.png")

        # Change the size of the Sprite.
        self.scale = 0.2

        # Set the initial position of the player.
        self.center_x = 400
        self.center_y = 300

        # Store the player's movement speed.
        self.speed = PLAYER_SPEED

        # Store the current movement value on the X and Y axes.
        self.change_x = 0
        self.change_y = 0

        # Store the current state of each movement key.
        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False

        # Create a Health for player
        self.health = PLAYER_HEALTH

        # Create a Damage for player
        self.damage = PLAYER_DAMAGE

    # keep player inside screen
    def keep_inside_screen(self):
        if self.left < 0:
            self.left = 0

        if self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH

        if self.bottom < 0:
            self.bottom = 0

        if self.top > SCREEN_HEIGHT:
            self.top = SCREEN_HEIGHT