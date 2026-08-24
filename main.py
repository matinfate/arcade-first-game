import arcade
import random

# Create a class named `Game` that inherits from `arcade.Window`.
class Game(arcade.Window):

    def __init__(self):
        # Initialize the parent class (`arcade.Window`).
        super().__init__(800, 600, "My First Game")

        # Create a Sprite using the player image.
        self.player = arcade.Sprite("player.png")

        # Change the size of the Sprite.
        self.player.scale = 0.2

        # Set the initial position of the player.
        self.player.center_x = 400
        self.player.center_y = 300

        # Create a SpriteList to store our sprites.
        self.player_list = arcade.SpriteList() # SpriteList is a specialized Arcade list for storing sprites.

        # Add the player Sprite to the SpriteList.
        self.player_list.append(self.player)

        # Add the enemy Sprite to the SpriteList.
        self.enemy_list = arcade.SpriteList()

        # Creating an enemy to start the game
        for i in range(5):
            self.create_enemy()

        # Create a SpriteList for Storing bullets
        self.bullet_list = arcade.SpriteList()

        # Create a Damage for player
        self.damage=20

        # Create invincible system
        self.invincible=False
        self.invincibility_time=1.0
        self.invincibility_timer=0

        # Create a Score system
        self.score=0

        # Create a Health for player
        self.health = 100

        # Create a game over variable
        self.game_over = False

        # Store the player's movement speed.
        self.speed = 200

        # Store the current movement value on the X and Y axes.
        self.change_x = 0
        self.change_y = 0

        # Store the current state of each movement key.
        # False means that the key is not currently being held.
        self.up_pressed = False
        self.down_pressed = False
        self.left_pressed = False
        self.right_pressed = False

    def on_draw(self):
        # `on_draw` is a method specific to Arcade.
        # Arcade calls it when it needs to draw a new frame.

        # Clear the previous frame.
        self.clear()

        # Draw all sprites inside the SpriteList.
        self.player_list.draw()
        self.enemy_list.draw()
        self.bullet_list.draw()

        # Show score
        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 20)

        # Show health
        arcade.draw_text(f"Health: {self.health}",10, 40, arcade.color.RED,  20)

        # Show game over
        if self.game_over:
            arcade.draw_text("GAME OVER",270,300,arcade.color.RED_PURPLE,40)

    def on_update(self, delta_time):
        # `on_update` is used to update the game state.
        #
        # `delta_time` = the amount of time that has passed
        # since the previous call to on_update().

        # If the game is Game Over, the player, enemies, and bullets no longer move.
        if self.game_over:
            return

        # Damage cooldown
        if self.invincibility_timer>0:
            self.invincibility_timer -= delta_time

            # Blink player
            self.player.visible = int(self.invincibility_timer * 10) % 2 == 0

            if self.invincibility_timer<=0:
                self.invincible=False

        # Reset movement values at the beginning of each update.
        self.change_x = 0
        self.change_y = 0

        # If W is being held, move upward.
        if self.up_pressed:
            self.change_y = self.speed

        # If S is being held, move downward.
        if self.down_pressed:
            self.change_y = -self.speed

        # If D is being held, move right.
        if self.right_pressed:
            self.change_x = self.speed

        # If A is being held, move left.
        if self.left_pressed:
            self.change_x = -self.speed

        # Update the player's position.
        #
        # Instead of changing self.x and self.y,
        # we now change the Sprite's position.
        self.player.center_x += self.change_x * delta_time
        self.player.center_y += self.change_y * delta_time

        # Move enemy toward player
        for enemy in self.enemy_list:

            if enemy.center_x < self.player.center_x:
                enemy.center_x += 50 * delta_time

            elif enemy.center_x > self.player.center_x:
                enemy.center_x -= 50 * delta_time

            if enemy.center_y < self.player.center_y:
                enemy.center_y += 50 * delta_time

            elif enemy.center_y > self.player.center_y:
                enemy.center_y -= 50 * delta_time

            # If the enemy collides with the player,
            if arcade.check_for_collision(enemy,self.player):
                if not self.invincible:
                    self.health -= self.damage
                    self.invincible=True
                    self.invincibility_timer=self.invincibility_time
                    enemy.remove_from_sprite_lists()
                    self.create_enemy()

                if self.health == 0:
                    self.game_over = True


        # Move bullet
        for bullet in self.bullet_list:
            bullet.center_y+=bullet.change_y*delta_time
            # If the bullet collides with the enemy,
            hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)
            if hit_list:
                for enemy in hit_list:
                    self.score += 10 # Add score for kill enemy
                    enemy.remove_from_sprite_lists()
                    bullet.remove_from_sprite_lists()
                    self.create_enemy()

    # Keyboard key press event.
    def on_key_press(self, key, modifiers):

        # If W is pressed, set up_pressed to True.
        if key == arcade.key.W:
            self.up_pressed = True

        # If S is pressed, set down_pressed to True.
        if key == arcade.key.S:
            self.down_pressed = True

        # If A is pressed, set left_pressed to True.
        if key == arcade.key.A:
            self.left_pressed = True

        # If D is pressed, set right_pressed to True.
        if key == arcade.key.D:
            self.right_pressed = True

        # If Space pressed,create a bullet
        if key == arcade.key.SPACE:
            bullet=arcade.Sprite("bullet.png")
            bullet.scale = 0.2
            bullet.center_x = self.player.center_x
            bullet.bottom=self.player.top
            bullet.change_y = 500
            self.bullet_list.append(bullet)

        # If R pressed. Restart game
        if key == arcade.key.R:
            self.restart_game()

    # Keyboard key release event.
    def on_key_release(self, key, modifiers):

        # If W is released, set up_pressed to False.
        if key == arcade.key.W:
            self.up_pressed = False

        # If S is released, set down_pressed to False.
        if key == arcade.key.S:
            self.down_pressed = False

        # If A is released, set left_pressed to False.
        if key == arcade.key.A:
            self.left_pressed = False

        # If D is released, set right_pressed to False.
        if key == arcade.key.D:
            self.right_pressed = False

    # Generate enemy automote
    def create_enemy(self):
        enemy=arcade.Sprite("enemy.png")
        enemy.scale=0.2
        enemy.center_x = random.randint(50,750)
        enemy.center_y = random.randint(400,550)
        self.enemy_list.append(enemy)

    # Restart game
    def restart_game(self):
        self.player.center_x=400
        self.player.center_y=300

        self.health = 100
        self.score = 0
        self.invincibility_timer=0
        self.invincible=False
        self.game_over = False

        self.bullet_list.clear()
        self.enemy_list.clear()

        for i in range(5):
            self.create_enemy()

# Create an object (instance) of the Game class.
game = Game()

# Start the Arcade Game/Event Loop.
arcade.run()