# Arcade First Game

A 2D arcade shooter built with Python and the Arcade library.

This project was created as a learning project to practice Python, object-oriented programming, game development, and basic game architecture.

## Features

* 2D arcade shooter gameplay
* WASD player movement
* Spacebar shooting
* Shooting cooldown system
* Rapid Fire power-up
* Player health system
* Shield power-up
* Health power-up
* Temporary invincibility after taking damage
* Multiple enemy types:

  * Normal Enemy
  * Fast Enemy
  * Tank Enemy
* Enemy health and damage systems
* Enemy health bars
* Enemy collision avoidance
* Tank enemy knockback
* Fast enemy zigzag movement
* Safe enemy spawning
* Wave-based progression
* Increasing number of enemies per wave
* Increasing enemy difficulty
* Dynamic enemy type probabilities
* Score system
* Kill counter
* Persistent local High Score
* Game Over screen
* Game restart system
* Pause / Resume system
* Wave completion countdown
* Explosion effects
* Particle effects
* Damage numbers
* Health, Shield, and Rapid Fire status bars
* Sound effects
* Background music
* Separate music and sound-effect volume control
* Background music lifecycle management
* Main menu
* Centered game window

## Controls

| Key   | Action                  |
| ----- | ----------------------- |
| W     | Move Up                 |
| A     | Move Left               |
| S     | Move Down               |
| D     | Move Right              |
| Space | Shoot                   |
| ESC   | Pause / Resume          |
| R     | Restart after Game Over |

## Gameplay

The player starts with a limited amount of health and must survive increasingly difficult waves of enemies.

Enemies move toward the player and deal damage on collision.

Different enemy types have different characteristics.

### Normal Enemy

The standard enemy type.

* Balanced speed
* Standard health
* Standard damage
* Standard score

### Fast Enemy

A faster and weaker enemy.

* High movement speed
* Lower health
* Higher score
* Zigzag movement pattern

### Tank Enemy

A slower but stronger enemy.

* Low movement speed
* High health
* High damage
* Higher score
* Can knock the player back

As the wave number increases, the game gradually increases the difficulty by spawning more enemies and changing the probability of enemy types.

## Wave System

The game starts with:

* Wave 1
* 5 enemies

After completing a wave, the game waits briefly before starting the next wave.

Each new wave increases the number of enemies.

Enemy probabilities also change as the wave number increases, making Fast and Tank enemies more common during later waves.

A short countdown is displayed between waves.

## Power-Ups

Enemies have a chance to drop a power-up when defeated.

There are three types of power-ups.

### Health

Restores part of the player's health without exceeding maximum health.

### Shield

Temporarily protects the player from damage.

### Rapid Fire

Temporarily reduces the shooting cooldown, allowing the player to fire much faster.

Active temporary power-ups are displayed on the HUD with status bars and timers.

## Combat and Effects

The game includes several visual effects to make combat more dynamic.

### Explosions

Enemies create an explosion effect when destroyed.

### Particles

Particle effects are generated when enemies are destroyed.

### Damage Numbers

Damage values can be displayed when enemies are hit.

### Enemy Health Bars

Enemy health bars visually indicate how much health remains.

## Audio

The game includes:

* Shooting sound
* Enemy death sound
* Player hit sound
* Power-up sound
* Wave start sound
* Game Over sound
* Background music

Background music loops during gameplay and is stopped when the game ends.

Music and sound effects use separate volume settings.

## Score System

The player earns points by defeating enemies.

Different enemy types award different amounts of score.

The HUD displays:

* Score
* Kill count
* Current wave
* Player health
* Active power-up timers

## High Score

The highest score is saved locally on the player's computer.

The file is stored at:

```text
data/high_score.txt
```

The High Score file is not included in version control because each player should have their own record.

If the `data` directory does not exist, the game creates it automatically when the High Score is first saved.

This means a new player starts with a High Score of `0`, while returning players keep their own previous record.

## Pause / Resume

Press:

```text
ESC
```

during gameplay to pause or resume the game.

While paused, the game logic stops until the player resumes the game.

## Game Over

When the player's health reaches zero, the game enters the Game Over state.

The Game Over screen displays:

* Current score
* High Score
* Kill count
* Restart option

The background music stops and the Game Over sound is played.

Press `R` to restart the game.

## Project Structure

```text
arcade-first-game/
│
├── assets/
│   ├── image/
│   │   ├── bullet.png
│   │   ├── enemy.png
│   │   ├── fast_enemy.png
│   │   ├── health_powerup.png
│   │   ├── player.png
│   │   ├── rapid_fire_powerup.png
│   │   ├── shield_powerup.png
│   │   └── tank_enemy.png
│   │
│   └── sound/
│       ├── background_music.ogg
│       ├── enemy_death.wav
│       ├── game_over.wav
│       ├── player_hit.wav
│       ├── power_up.wav
│       ├── shoot.wav
│       └── wave_start.wav
│
├── config/
│   └── settings.py
│
├── data/
│   └── high_score.txt
│
├── entities/
│   ├── bullet.py
│   ├── damage_number.py
│   ├── enemy.py
│   ├── explosion.py
│   ├── particle.py
│   ├── player.py
│   └── power_up.py
│
├── systems/
│   └── sound_manager.py
│
├── game.py
├── main.py
├── .gitignore
└── README.md
```

## Architecture

The project is divided into several logical sections.

### `game.py`

Contains the main game controller and manages:

* Game states
* Player
* Enemies
* Bullets
* Power-ups
* Waves
* Score
* Collisions
* HUD
* Game Over
* Pause
* Game restart

### `entities/`

Contains the main gameplay objects:

* `player.py` — Player
* `enemy.py` — Enemy classes
* `bullet.py` — Bullets
* `power_up.py` — Power-ups
* `explosion.py` — Explosion effects
* `particle.py` — Particle effects
* `damage_number.py` — Damage number effects

### `systems/`

Contains reusable game systems.

Currently:

```text
sound_manager.py
```

is responsible for loading and playing sound effects and background music.

### `config/`

Contains centralized game settings such as:

* Screen size
* Player settings
* Enemy settings
* Wave settings
* Bullet settings
* Shooting cooldown
* Power-up durations
* Particle settings

### `data/`

Contains locally generated game data.

The High Score file is intentionally ignored by Git so each player can have their own record.

### `assets/`

Contains game resources such as images and sounds.

## Requirements

* Python 3.11+
* Arcade

## Installation

Clone the repository:

```bash
git clone https://github.com/matinfate/arcade-first-game.git
```

Enter the project directory:

```bash
cd arcade-first-game
```

Install Arcade:

```bash
pip install arcade
```

## Running the Game

Run:

```bash
python main.py
```

The main menu will appear when the game starts.

Press:

```text
SPACE
```

to start the game.

## Technologies

* Python
* Arcade
* Object-Oriented Programming
* Git
* GitHub

## Project Goals

This project was created primarily for learning and practicing:

* Python programming
* Object-oriented programming
* Game development
* Game loops
* Collision detection
* Sprite management
* Game states
* Game architecture
* Audio management
* Basic visual effects
* File-based data persistence
* Git and GitHub workflow

## Project Status

**Version 1.0 — Complete**

The first playable version of the game is complete and includes the core gameplay systems, multiple enemy types, wave progression, power-ups, audio, visual effects, scoring, High Score persistence, pause/resume, restart, and Game Over functionality.

Future development can focus on additional gameplay mechanics, balancing, visual polish, content, and new features.
