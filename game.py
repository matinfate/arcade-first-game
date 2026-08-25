import arcade

from player import Player
from enemy import Enemy
from bullet import Bullet

# Create a class named `Game` that inherits from `arcade.Window`.
class Game(arcade.Window):

    def __init__(self):
        # Initialize the parent class (`arcade.Window`).
        super().__init__(800, 600, "My First Game")

        # Create a player from class Player.
        self.player = Player()

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


        # Create invincible system
        self.invincible=False
        self.invincibility_time=1.0
        self.invincibility_timer=0

        # Create cooldown system for bullet
        self.shoot_cooldown=0.25
        self.shoot_timer=0

        # Create a Score system
        self.score=0


        # Create a game over variable
        self.game_over = False

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
        arcade.draw_text(f"Health: {self.player.health}",10, 40, arcade.color.RED,  20)

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
                self.player.visible = True

        # Shoot cooldown
        if self.shoot_timer>0:
            self.shoot_timer -= delta_time

        # Reset movement values at the beginning of each update.
        self.player.change_x = 0
        self.player.change_y = 0

        # If W is being held, move upward.
        if self.player.up_pressed:
            self.player.change_y = self.player.speed

        # If S is being held, move downward.
        if self.player.down_pressed:
            self.player.change_y = -self.player.speed

        # If D is being held, move right.
        if self.player.right_pressed:
            self.player.change_x = self.player.speed

        # If A is being held, move left.
        if self.player.left_pressed:
            self.player.change_x = -self.player.speed

        # Update the player's position.
        # Instead of changing self.x and self.y,
        # we now change the Sprite's position.
        self.player.center_x += self.player.change_x * delta_time
        self.player.center_y += self.player.change_y * delta_time

        # Move enemy toward player
        for enemy in self.enemy_list:

            if enemy.center_x < self.player.center_x:
                enemy.center_x += enemy.speed * delta_time

            elif enemy.center_x > self.player.center_x:
                enemy.center_x -= enemy.speed * delta_time

            if enemy.center_y < self.player.center_y:
                enemy.center_y += enemy.speed * delta_time

            elif enemy.center_y > self.player.center_y:
                enemy.center_y -= enemy.speed * delta_time

            # If the enemy collides with the player,
            if arcade.check_for_collision(enemy,self.player):
                if not self.invincible:
                    self.player.health -= self.player.damage
                    self.invincible=True
                    self.invincibility_timer=self.invincibility_time
                    enemy.remove_from_sprite_lists()
                    self.create_enemy()

                if self.player.health <= 0:
                    self.game_over = True


        # Move bullet
        for bullet in self.bullet_list:
            bullet.center_y += bullet.speed * delta_time

            # Remove bullets that leave the screen
            if bullet.bottom > self.height:
                bullet.remove_from_sprite_lists()

            # Check bullet collision with enemies
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
            self.player.up_pressed = True

        # If S is pressed, set down_pressed to True.
        if key == arcade.key.S:
            self.player.down_pressed = True

        # If A is pressed, set left_pressed to True.
        if key == arcade.key.A:
            self.player.left_pressed = True

        # If D is pressed, set right_pressed to True.
        if key == arcade.key.D:
            self.player.right_pressed = True

        # If Space pressed,create a bullet
        if key == arcade.key.SPACE and self.shoot_timer <= 0:
            bullet = Bullet(self.player.center_x,self.player.top)

            self.bullet_list.append(bullet)
            self.shoot_timer = self.shoot_cooldown

        # If R pressed. Restart game
        if key == arcade.key.R and self.game_over:
            self.restart_game()

    # Keyboard key release event.
    def on_key_release(self, key, modifiers):

        # If W is released, set up_pressed to False.
        if key == arcade.key.W:
            self.player.up_pressed = False

        # If S is released, set down_pressed to False.
        if key == arcade.key.S:
            self.player.down_pressed = False

        # If A is released, set left_pressed to False.
        if key == arcade.key.A:
            self.player.left_pressed = False

        # If D is released, set right_pressed to False.
        if key == arcade.key.D:
            self.player.right_pressed = False

    # Generate enemy automote
    def create_enemy(self):
        enemy = Enemy()
        self.enemy_list.append(enemy)

    # Restart game
    def restart_game(self):
        self.player.health = 100
        self.score = 0
        self.invincibility_timer = 0
        self.invincible = False
        self.game_over = False
        self.player.visible = True

        self.bullet_list.clear()
        self.enemy_list.clear()

        for i in range(5):
            self.create_enemy()