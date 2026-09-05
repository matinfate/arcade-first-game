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

class Game(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TITLE)


        self.player = Player()


        self.player_list = arcade.SpriteList() # SpriteList is a specialized Arcade list for storing sprites.


        self.player_list.append(self.player)


        self.enemy_list = arcade.SpriteList()

        # Wave settings
        self.wave = 1
        self.enemy_count = 5

        # Wave transition timer
        self.wave_delay = 2.0
        self.wave_timer = 0
        self.wave_complete = False

        # Create the first enemy wave
        for i in range(self.enemy_count):
            self.create_enemy()

        # Sprite list for bullets
        self.bullet_list = arcade.SpriteList()

        # Lists for explosions and particles
        self.explosion_list = []
        self.particles = []

        # Player invincibility
        self.invincible=False
        self.invincibility_time=INVINCIBILITY_TIME
        self.invincibility_timer=0

        # Shooting cooldown
        self.shoot_cooldown=SHOOT_COOLDOWN
        self.shoot_timer=0

        # Game statistics
        self.score=0
        self.kills = 0

        # Game states
        self.game_started=False
        self.paused = False
        self.game_over = False

    def on_draw(self):
        self.clear()

        # Main menu
        if not self.game_started:
            arcade.draw_text("ARCADE GAME",SCREEN_WIDTH / 2,350,arcade.color.WHITE,40,anchor_x="center")
            arcade.draw_text("Press SPACE to Start",SCREEN_WIDTH / 2,280,arcade.color.YELLOW,20,anchor_x="center")
            arcade.draw_text("WASD: Move",SCREEN_WIDTH / 2,220,arcade.color.WHITE,18,anchor_x="center")
            arcade.draw_text("SPACE: Shoot",SCREEN_WIDTH / 2,190,arcade.color.WHITE,18,anchor_x="center")
            return

        # Draw game sprites
        self.player_list.draw()
        self.enemy_list.draw()
        self.bullet_list.draw()

        # Pause menu
        if self.paused:
            arcade.draw_text("PAUSED",SCREEN_WIDTH/2,300,arcade.color.YELLOW,40,anchor_x="center")
            arcade.draw_text("Press ESC to Resume",SCREEN_WIDTH/2,250,arcade.color.WHITE,20,anchor_x="center")

        # Display score
        arcade.draw_text(f"Score: {self.score}", 10, 570, arcade.color.WHITE, 20)

        # Display kill count
        arcade.draw_text(f"Kills: {self.kills}", 10, 500, arcade.color.WHITE, 20)

        # Draw enemy health bars
        for enemy in self.enemy_list:
            enemy.draw_health_bar()

        # Draw explosions
        for explosion in self.explosion_list:
            explosion.draw()

        # Draw particles
        for particle in self.particles:
            particle.draw()

        # Draw player health bar
        max_health=PLAYER_HEALTH
        health_x = 110
        health_width=200
        health_height=20
        health_ratio=self.player.health/max_health
        current_health_width = health_width * health_ratio

        arcade.draw_rect_filled( # This defines Fill and color this rectangle.
            arcade.rect.XYWH( # This defines a rectangle.
                health_x,
                40,
                health_width,
                health_height
            ),
            arcade.color.DARK_RED
        )  # Health bar background

        arcade.draw_rect_filled(
            arcade.rect.XYWH(
                10 + current_health_width / 2,
                40,
                current_health_width,
                health_height
            ),
            arcade.color.GREEN
        )  # Current health

        # Display current wave
        arcade.draw_text(f"Wave:{self.wave}",10, 530, arcade.color.DARK_RED, 20)

        # Display wave completion message
        if self.wave_complete and not self.game_over:
            arcade.draw_text(
                f"Wave {self.wave} Complete!",
                250,
                300,
                arcade.color.YELLOW,
                30
            )

        # Game over screen
        if self.game_over:
            arcade.draw_text("GAME OVER",SCREEN_WIDTH/2,300,arcade.color.RED_PURPLE,40,anchor_x="center")
            arcade.draw_text("Press R to Restart",SCREEN_WIDTH/2,250,arcade.color.WHITE,20,anchor_x="center")

    def on_update(self, delta_time):

        # Stop updates when the game is inactive
        if self.game_over or not self.game_started or self.paused:
            return

        # Update invincibility timer
        if self.invincibility_timer>0:
            self.invincibility_timer -= delta_time

            # Blink player
            self.player.visible = int(self.invincibility_timer * 10) % 2 == 0

            if self.invincibility_timer<=0:
                self.invincible=False
                self.player.visible = True

        # Update shooting cooldown
        if self.shoot_timer>0:
            self.shoot_timer -= delta_time

        # Reset movement
        self.player.change_x = 0
        self.player.change_y = 0

        # Handle movement input
        if self.player.up_pressed:
            self.player.change_y = self.player.speed

        if self.player.down_pressed:
            self.player.change_y = -self.player.speed

        if self.player.right_pressed:
            self.player.change_x = self.player.speed

        if self.player.left_pressed:
            self.player.change_x = -self.player.speed

        # Update player position
        self.player.center_x += self.player.change_x * delta_time
        self.player.center_y += self.player.change_y * delta_time

        # Keep player inside the screen
        self.player.keep_inside_screen()

        # Move enemies toward the player
        for enemy in self.enemy_list:
            enemy.move_toward_player(self.player, delta_time)

            # Handle enemy-player collision
            if arcade.check_for_collision(enemy,self.player):
                if not self.invincible:
                    self.player.health = max(0,self.player.health - enemy.damage)
                    self.invincible=True
                    self.invincibility_timer=self.invincibility_time
                    enemy.remove_from_sprite_lists()
                    self.create_enemy()

                if self.player.health <= 0:
                    self.game_over = True

        # Prevent enemies from overlapping each other.
        for enemy in self.enemy_list:
            for other in self.enemy_list:
                if enemy!=other:
                    enemy.avoid_enemy(other,delta_time)

        # Move bullets
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
                        # Update score and kill count
                        self.score += enemy.score
                        self.kills+=1

                        # Create explosion effect
                        explosion=Explosion(enemy.center_x,enemy.center_y)

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

        # Check if the current wave is complete
        if len(self.enemy_list)==0:
            self.wave_complete=True
            self.wave_timer+=delta_time

            if self.wave_timer>=self.wave_delay:
                self.next_wave()
                self.wave_timer=0
                self.wave_complete = False

    def on_key_press(self, key, modifiers):

        if key == arcade.key.W:
            self.player.up_pressed = True

        if key == arcade.key.S:
            self.player.down_pressed = True

        if key == arcade.key.A:
            self.player.left_pressed = True

        if key == arcade.key.D:
            self.player.right_pressed = True

        # Start game
        if key == arcade.key.SPACE and not self.game_started:
            self.game_started = True
            return

        # Shoot
        if key == arcade.key.SPACE and self.shoot_timer <= 0 and not self.paused:
            bullet = Bullet(self.player.center_x, self.player.top)

            self.bullet_list.append(bullet)
            self.shoot_timer = self.shoot_cooldown

        # Toggle pause
        if key == arcade.key.ESCAPE and self.game_started and not self.game_over:
            self.paused = not self.paused

        # Restart game
        if key == arcade.key.R and self.game_over:
            self.restart_game()

    def on_key_release(self, key, modifiers):

        if key == arcade.key.W:
            self.player.up_pressed = False

        if key == arcade.key.S:
            self.player.down_pressed = False

        if key == arcade.key.A:
            self.player.left_pressed = False

        if key == arcade.key.D:
            self.player.right_pressed = False

    # Create a random enemy type
    def create_enemy(self):

        normal_chance = max(50, 70 - (self.wave - 1) * 5)
        fast_chance = min(25, 15 + (self.wave - 1) * 2)

        enemy_type = random.randint(1, 100)

        if enemy_type <= normal_chance:
            enemy = Enemy()

        elif enemy_type <= normal_chance + fast_chance:
            enemy = FastEnemy()

        else:
            enemy = TankEnemy()

        # Set a safe spawn position away from the player.
        while True:
            enemy.center_x = random.randint(50, SCREEN_WIDTH - 50)
            enemy.center_y = random.randint(350, SCREEN_HEIGHT - 50)

            if not arcade.check_for_collision(enemy, self.player):
                break

        self.enemy_list.append(enemy)



    # Start the next wave
    def next_wave(self):
        self.wave += 1

        self.enemy_count += 2

        for i in range(self.enemy_count):
            self.create_enemy()

    # Reset the game state
    def restart_game(self):
        self.player.health = PLAYER_HEALTH
        self.score = 0
        self.kills = 0

        self.invincibility_timer = 0
        self.shoot_timer = 0

        self.invincible = False
        self.game_over = False
        self.paused = False

        self.wave_complete = False
        self.wave_timer = 0

        self.player.visible = True

        self.wave = 1
        self.enemy_count = 5

        self.player.center_x = self.player.start_x
        self.player.center_y = self.player.start_y

        self.bullet_list.clear()
        self.enemy_list.clear()

        for i in range(self.enemy_count):
            self.create_enemy()