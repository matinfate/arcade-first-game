import arcade
import random

from player import Player
from enemy import Enemy, FastEnemy, TankEnemy
from bullet import Bullet
from explosion import Explosion
from particle import Particle
from power_up import HealthPowerUp, ShieldPowerUp, RapidFirePowerUp

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

        # Create a list to store health power-ups.
        self.power_up_list = arcade.SpriteList()

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

    def draw_main_menu(self):

        arcade.draw_text(
            "ARCADE GAME",
            SCREEN_WIDTH / 2,
            350,
            arcade.color.WHITE,
            40,
            anchor_x="center"
        )

        arcade.draw_text(
            "Press SPACE to Start",
            SCREEN_WIDTH / 2,
            280,
            arcade.color.YELLOW,
            20,
            anchor_x="center"
        )

        arcade.draw_text(
            "WASD: Move",
            SCREEN_WIDTH / 2,
            220,
            arcade.color.WHITE,
            18,
            anchor_x="center"
        )

        arcade.draw_text(
            "SPACE: Shoot",
            SCREEN_WIDTH / 2,
            190,
            arcade.color.WHITE,
            18,
            anchor_x="center"
        )

    def draw_game_objects(self):

        # Draw player
        self.player_list.draw()

        # Draw player shield
        if self.player.shield_active:
            arcade.draw_circle_outline(
                self.player.center_x,
                self.player.center_y,
                self.player.width * 0.7,
                arcade.color.BLUE,
                3
            )

        # Draw enemies
        self.enemy_list.draw()

        # Draw bullets
        self.bullet_list.draw()

        # Draw power-ups
        self.power_up_list.draw()

        # Draw enemy health bars
        for enemy in self.enemy_list:
            enemy.draw_health_bar()

        # Draw explosions
        for explosion in self.explosion_list:
            explosion.draw()

        # Draw particles
        for particle in self.particles:
            particle.draw()

    def draw_game_ui(self):

        # Display score
        arcade.draw_text(
            f"Score: {self.score}",
            10,
            570,
            arcade.color.WHITE,
            20
        )

        # Display kill count
        arcade.draw_text(
            f"Kills: {self.kills}",
            10,
            500,
            arcade.color.WHITE,
            20
        )

        # Draw player health bar
        max_health = PLAYER_HEALTH
        health_x = 110
        health_width = 200
        health_height = 20
        health_ratio = self.player.health / max_health
        current_health_width = health_width * health_ratio

        arcade.draw_rect_filled(
            arcade.rect.XYWH(
                health_x,
                40,
                health_width,
                health_height
            ),
            arcade.color.DARK_RED
        )

        arcade.draw_rect_filled(
            arcade.rect.XYWH(
                10 + current_health_width / 2,
                40,
                current_health_width,
                health_height
            ),
            arcade.color.GREEN
        )

        # Display current wave
        arcade.draw_text(
            f"Wave:{self.wave}",
            10,
            530,
            arcade.color.DARK_RED,
            20
        )

    def draw_power_up_bars(self):

        bar_x = 10
        bar_width = 200
        bar_height = 20

        # Shield Bar
        if self.player.shield_active:
            max_duration = 5.0
            ratio = max(0, self.player.shield_timer / max_duration)
            current_width = bar_width * ratio

            arcade.draw_rect_filled(
                arcade.rect.XYWH(
                    bar_x + bar_width / 2,
                    110,
                    bar_width,
                    bar_height
                ),
                arcade.color.DARK_BLUE
            )

            arcade.draw_rect_filled(
                arcade.rect.XYWH(
                    bar_x + current_width / 2,
                    110,
                    current_width,
                    bar_height
                ),
                arcade.color.BLUE
            )

            arcade.draw_text(
                f"{max(0, self.player.shield_timer):.1f}s",
                bar_x + bar_width / 2,
                102,
                arcade.color.WHITE,
                14,
                anchor_x="center"
            )

        # Rapid Fire Bar
        if self.player.rapid_fire_active:
            max_duration = 5.0
            ratio = max(0, self.player.rapid_fire_timer / max_duration)
            current_width = bar_width * ratio

            arcade.draw_rect_filled(
                arcade.rect.XYWH(
                    bar_x + bar_width / 2,
                    80,
                    bar_width,
                    bar_height
                ),
                arcade.color.DARK_ORANGE
            )

            arcade.draw_rect_filled(
                arcade.rect.XYWH(
                    bar_x + current_width / 2,
                    80,
                    current_width,
                    bar_height
                ),
                arcade.color.ORANGE
            )

            arcade.draw_text(
                f"{max(0, self.player.rapid_fire_timer):.1f}s",
                bar_x + bar_width / 2,
                72,
                arcade.color.WHITE,
                14,
                anchor_x="center"
            )

    def draw_pause_menu(self):

        arcade.draw_text(
            "PAUSED",
            SCREEN_WIDTH / 2,
            300,
            arcade.color.YELLOW,
            40,
            anchor_x="center"
        )

        arcade.draw_text(
            "Press ESC to Resume",
            SCREEN_WIDTH / 2,
            250,
            arcade.color.WHITE,
            20,
            anchor_x="center"
        )

    def draw_wave_complete(self):

        arcade.draw_text(
            f"Wave {self.wave} Complete!",
            250,
            300,
            arcade.color.YELLOW,
            30
        )

    def draw_game_over(self):

        arcade.draw_text(
            "GAME OVER",
            SCREEN_WIDTH / 2,
            300,
            arcade.color.RED_PURPLE,
            40,
            anchor_x="center"
        )

        arcade.draw_text(
            "Press R to Restart",
            SCREEN_WIDTH / 2,
            250,
            arcade.color.WHITE,
            20,
            anchor_x="center"
        )

    def on_draw(self):
        self.clear()

        if not self.game_started:
            self.draw_main_menu()
            return

        self.draw_game_objects()
        self.draw_game_ui()
        self.draw_power_up_bars()

        # Pause menu
        if self.paused:
            self.draw_pause_menu()

        # Display wave completion message
        if self.wave_complete and not self.game_over:
            self.draw_wave_complete()

        # Game over screen
        if self.game_over:
            self.draw_game_over()

    def update_timers(self,delta_time):

        # Update invincibility timer
        if self.invincibility_timer > 0:
            self.invincibility_timer -= delta_time

            # Blink player
            self.player.visible = int(self.invincibility_timer * 10) % 2 == 0

            if self.invincibility_timer <= 0:
                self.invincible = False
                self.player.visible = True

        # Update shooting cooldown
        if self.shoot_timer > 0:
            self.shoot_timer -= delta_time

        # Shield Time Management
        if self.player.shield_active:
            self.player.shield_timer -= delta_time

            if self.player.shield_timer <= 0:
                self.player.shield_active = False
                self.player.shield_timer = 0

        # Rapid fire time management
        if self.player.rapid_fire_active:
            self.player.rapid_fire_timer -= delta_time

            if self.player.rapid_fire_timer <= 0:
                self.player.rapid_fire_active = False
                self.player.rapid_fire_timer = 0

    def update_player(self, delta_time):

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

    def update_enemies(self, delta_time):

        # Move enemies toward the player
        for enemy in self.enemy_list:
            enemy.move_toward_player(self.player, delta_time)

            # Handle enemy-player collision
            if arcade.check_for_collision(enemy, self.player):
                if self.player.shield_active:
                    enemy.remove_from_sprite_lists()
                    self.create_enemy()

                elif not self.invincible:
                    self.player.health = max(0, self.player.health - enemy.damage)

                    # Tank knockback
                    if isinstance(enemy, TankEnemy):
                        dx = self.player.center_x - enemy.center_x
                        dy = self.player.center_y - enemy.center_y
                        distance = (dx ** 2 + dy ** 2) ** 0.5

                        if distance > 0:
                            self.player.center_x += (dx / distance * enemy.knockback)
                            self.player.center_y += (dy / distance * enemy.knockback)
                            self.player.keep_inside_screen()

                    self.invincible = True
                    self.invincibility_timer = self.invincibility_time

                    enemy.remove_from_sprite_lists()
                    self.create_enemy()

                    if self.player.health <= 0:
                        self.game_over = True

        # Prevent enemies from overlapping each other.
        for i in range(len(self.enemy_list)):
            enemy = self.enemy_list[i]

            for j in range(i + 1, len(self.enemy_list)):
                other = self.enemy_list[j]
                enemy.avoid_enemy(other, delta_time)
                other.avoid_enemy(enemy, delta_time)

    def update_bullets(self, delta_time):

        # Move bullets
        for bullet in self.bullet_list:
            bullet.center_y += bullet.speed * delta_time

            # Remove bullets that leave the screen
            if bullet.bottom > self.height:
                bullet.remove_from_sprite_lists()

            # Check bullet collision with enemies
            hit_list = arcade.check_for_collision_with_list(bullet, self.enemy_list)
            if hit_list:
                enemy = hit_list[0]
                enemy.health -= BULLET_DAMAGE
                bullet.remove_from_sprite_lists()

                if enemy.health <= 0:
                    # Update score and kill count
                    self.score += enemy.score
                    self.kills += 1

                    # Spawn a  power-up with a 20% chance
                    if random.random() < 0.2:
                        power_up_type = random.choice([HealthPowerUp, RapidFirePowerUp, ShieldPowerUp])
                        power_up = power_up_type()
                        power_up.center_x = enemy.center_x
                        power_up.center_y = enemy.center_y
                        self.power_up_list.append(power_up)

                    # Create explosion effect
                    explosion = Explosion(enemy.center_x, enemy.center_y)

                    for i in range(PARTICLE_COUNT):  # Create Particle
                        particle = Particle(
                            enemy.center_x,
                            enemy.center_y
                        )
                        self.particles.append(particle)

                    self.explosion_list.append(explosion)
                    enemy.remove_from_sprite_lists()

    def update_effects(self, delta_time):

        # Update explosions
        for explosion in self.explosion_list[:]:
            if explosion.update(delta_time):
                self.explosion_list.remove(explosion)

        # Update particles
        for particle in self.particles[:]:
            should_remove=particle.update(delta_time)

            if should_remove:
                self.particles.remove(particle)

    def update_power_ups(self,delta_time):

        # Move power-ups downward.
        for power_up in self.power_up_list:
            power_up.fall(delta_time)

            # Remove power-up when it leaves the screen
            if power_up.top < 0:
                power_up.remove_from_sprite_lists()
                continue

            # Check collision with player
            if arcade.check_for_collision(power_up, self.player):
                power_up.collect(self.player)
                power_up.remove_from_sprite_lists()

    def update_wave(self,delta_time):

        # Check if the current wave is complete
        if len(self.enemy_list)==0:
            self.wave_complete=True
            self.wave_timer+=delta_time

            if self.wave_timer>=self.wave_delay:
                self.next_wave()
                self.wave_timer=0
                self.wave_complete = False

    def on_update(self, delta_time):

        # Stop updates when the game is inactive
        if self.game_over or not self.game_started or self.paused:
            return

        self.update_timers(delta_time)
        self.update_player(delta_time)
        self.update_enemies(delta_time)
        self.update_bullets(delta_time)
        self.update_effects(delta_time)
        self.update_power_ups(delta_time)
        self.update_wave(delta_time)

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

            if self.player.rapid_fire_active:
                self.shoot_timer = self.shoot_cooldown / 3
            else:
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
        max_attempts = 100
        spawned_safely = False

        for _ in range(max_attempts):
            enemy.center_x = random.randint(50, SCREEN_WIDTH - 50)
            enemy.center_y = random.randint(350, SCREEN_HEIGHT - 50)

            dx=enemy.center_x - self.player.center_x
            dy=enemy.center_y - self.player.center_y
            distance=(dx ** 2 + dy ** 2) ** 0.5

            if distance >= 150:
                spawned_safely = True
                break

        if not spawned_safely:
            enemy.center_x = SCREEN_WIDTH - 50
            enemy.center_y = SCREEN_HEIGHT - 50

        self.enemy_list.append(enemy)

    # Start the next wave
    def next_wave(self):
        self.wave += 1

        self.enemy_count += 2

        for i in range(self.enemy_count):
            self.create_enemy()

    def reset_wave(self):
        self.wave = 1
        self.enemy_count = 5
        self.wave_complete = False
        self.wave_timer = 0

    # Reset the game state
    def restart_game(self):

        self.player.reset()
        self.score = 0
        self.kills = 0

        self.invincibility_timer = 0
        self.shoot_timer = 0

        self.invincible = False

        self.game_over = False
        self.paused = False

        self.reset_wave()

        self.bullet_list.clear()
        self.enemy_list.clear()
        self.power_up_list.clear()

        for i in range(self.enemy_count):
            self.create_enemy()