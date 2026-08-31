import arcade
import random

from player import Player
from enemy import Enemy, FastEnemy, TankEnemy
from bullet import Bullet
from explosion import Explosion
from particle import Particle

from settings import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    SCREEN_TITLE,
    SHOOT_COOLDOWN,
    INVINCIBILITY_TIME,
    PLAYER_HEALTH,
    BULLET_DAMAGE,
    PARTICLE_COUNT
)

# Create a class named `Game` that inherits from `arcade.Window`.
class Game(arcade.Window):

    def __init__(self):
        # Initialize the parent class (`arcade.Window`).
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)

        # Create a player from class Player.
        self.player = Player()

        # Create a SpriteList to store our sprites.
        self.player_list = arcade.SpriteList() # SpriteList is a specialized Arcade list for storing sprites.

        # Add the player Sprite to the SpriteList.
        self.player_list.append(self.player)

        # Add the enemy Sprite to the SpriteList.
        self.enemy_list = arcade.SpriteList()

        # Add enemy wave
        self.wave = 1
        self.enemy_count = 5

        # Add cooldown for next wave
        self.wave_delay = 2.0
        self.wave_timer = 0

        # Variable for Complete wave
        self.wave_complete = False

        # Creating an enemy to start the game
        for i in range(self.enemy_count):
            self.create_enemy()

        # Create a SpriteList for Storing bullets
        self.bullet_list = arcade.SpriteList()

        # Create a list for Storing explosion
        self.explosion_list = []

        # Create a list for Storing particles
        self.particles = []

        # Create invincible system
        self.invincible=False
        self.invincibility_time=INVINCIBILITY_TIME
        self.invincibility_timer=0

        # Create cooldown system for bullet
        self.shoot_cooldown=SHOOT_COOLDOWN
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
        arcade.draw_text(f"Score: {self.score}", 10, 570, arcade.color.WHITE, 20)

        # Show enemy health bar
        for enemy in self.enemy_list:
            enemy.draw_health_bar()

        # Show explosion
        for explosion in self.explosion_list:
            explosion.draw()

        # Show partile
        for particle in self.particles:
            particle.draw()

        # Show player health bar
        max_health=PLAYER_HEALTH
        health_width=200
        health_height=20
        health_ratio=self.player.health/max_health
        current_health_width = health_width * health_ratio

        arcade.draw_rect_filled( # This defines Fill and color this rectangle.
            arcade.rect.XYWH( # This defines a rectangle.
                10,
                40,
                health_width,
                health_height
            ),
            arcade.color.DARK_RED
        )  # Background

        arcade.draw_rect_filled(
            arcade.rect.XYWH(
                10,
                40,
                current_health_width,
                health_height
            ),
            arcade.color.GREEN
        )  # Current health


        # Show enemy wave
        arcade.draw_text(f"Wave:{self.wave}",10, 530, arcade.color.DARK_RED, 20)

        # Show complate wave
        if self.wave_complete and not self.game_over:
            arcade.draw_text(
                f"Wave {self.wave} Complete!",
                250,
                300,
                arcade.color.YELLOW,
                30
            )

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

        # keep player inside screen
        self.player.keep_inside_screen()

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
                    self.player.health = max(0,self.player.health - enemy.damage)
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
                    enemy.health-=BULLET_DAMAGE
                    bullet.remove_from_sprite_lists()

                    if enemy.health<=0:
                        self.score += enemy.score  # Add score for kill enemy

                        explosion=Explosion(enemy.center_x,enemy.center_y) # Create Explosion

                        for i in range(PARTICLE_COUNT): # Create Particle
                            particle = Particle(
                                enemy.center_x,
                                enemy.center_y
                            )
                            self.particles.append(particle)

                        self.explosion_list.append(explosion)
                        enemy.remove_from_sprite_lists()

        # Update explosions
        for explosion in self.explosion_list[:]:
            if explosion.update(delta_time):
                self.explosion_list.remove(explosion)

        # Update particles
        for particle in self.particles[:]:
            should_remove=particle.update(delta_time)

            if should_remove:
                self.particles.remove(particle)


        if len(self.enemy_list)==0:
            self.wave_complete=True
            self.wave_timer+=delta_time

            if self.wave_timer>=self.wave_delay:
                self.next_wave()
                self.wave_timer=0
                self.wave_complete = False

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

        normal_chance = max(50, 70 - (self.wave - 1) * 5)
        fast_chance = min(25, 15 + (self.wave - 1) * 2)
        tank_chance = 100 - normal_chance - fast_chance

        enemy_type = random.randint(1, 100)

        if enemy_type <= normal_chance:
            enemy = Enemy()

        elif enemy_type <= normal_chance + fast_chance:
            enemy = FastEnemy()

        else:
            enemy = TankEnemy()

        self.enemy_list.append(enemy)

    # Generate next wave
    def next_wave(self):
        self.wave += 1

        self.enemy_count += 2

        for i in range(self.enemy_count):
            self.create_enemy()

    # Restart game
    def restart_game(self):
        self.player.health = PLAYER_HEALTH
        self.score = 0
        self.invincibility_timer = 0

        self.invincible = False
        self.game_over = False
        self.player.visible = True

        self.wave = 1
        self.enemy_count = 5

        self.player.center_x = self.player.start_x
        self.player.center_y = self.player.start_y

        self.bullet_list.clear()
        self.enemy_list.clear()

        for i in range(self.enemy_count):
            self.create_enemy()