# Arcade First Game

A 2D arcade shooter developed with Python and the [Arcade](https://api.arcade.academy/) framework.

This project was created as a practical software development project for learning and applying Python, Object-Oriented Programming (OOP), modular architecture, game-state management, collision systems, enemy behavior, resource management, audio systems, UI design, and application packaging.

---

## Overview

The game is structured around a central game controller, reusable game entities, centralized configuration, and dedicated systems.

Current functionality includes:

* Player movement and shooting
* Multiple enemy types
* Wave-based gameplay
* Enemy health and damage systems
* Enemy collision avoidance
* Safe enemy spawning
* Power-ups
* Collision handling
* Particle and explosion effects
* Damage numbers
* Score and kill tracking
* Persistent local High Score
* Player invincibility after taking damage
* Pause and Resume
* Wave completion countdown
* Game Over and Restart
* Background music and sound effects
* Centralized configuration
* PyInstaller-based Windows packaging

---

## Tech Stack

| Technology  | Version / Usage         |
| ----------- | ----------------------- |
| Python      | 3.11.2                  |
| Arcade      | 3.3.3                   |
| PyInstaller | Windows packaging       |
| Git         | Version control         |
| GitHub      | Repository hosting      |
| PyCharm     | Development environment |

---

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
│   ├── paths.py
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
├── ArcadeGame.spec
├── .gitignore
└── README.md
```

---

## Architecture

The project separates different responsibilities into dedicated modules.

### `game.py`

Main game controller responsible for:

* Game-state management
* Player and enemy lifecycle
* Wave management
* Collision handling
* Shooting
* Scoring
* Power-up handling
* Effects
* Rendering
* Game restart
* Game Over flow

### `entities/`

Contains the main game entities.

| Module             | Responsibility                           |
| ------------------ | ---------------------------------------- |
| `player.py`        | Player movement, health and player state |
| `enemy.py`         | Normal, Fast and Tank enemies            |
| `bullet.py`        | Bullet behavior and movement             |
| `power_up.py`      | Health, Shield and Rapid Fire power-ups  |
| `explosion.py`     | Explosion effects                        |
| `particle.py`      | Particle effects                         |
| `damage_number.py` | Damage number display                    |

### `systems/`

Contains reusable game systems.

`systems/sound_manager.py` manages:

* Background music
* Shooting sounds
* Enemy death sounds
* Player hit sounds
* Power-up sounds
* Wave start sounds
* Game Over sound

### `config/`

Contains centralized configuration and resource-path handling.

`config/settings.py` contains configuration for:

* Window
* Player
* Enemies
* Waves
* Bullets
* Shooting
* Power-ups
* Damage
* Particles
* UI

`config/paths.py` provides resource and data paths for source execution and PyInstaller builds.

---

## Game States

The game currently supports the following states:

```text
Main Menu
    │
    ▼
 Playing
    │
    ├── Pause ──────► Playing
    │
    ├── Wave Complete
    │
    └── Game Over
             │
             ▼
          Restart
             │
             ▼
          Playing
```

### Main Menu

The main menu displays:

* Game title
* Start instruction
* Controls
* Keyboard shortcuts

### Playing

The main gameplay state where the player moves, shoots, fights enemies, collects power-ups, and progresses through waves.

### Paused

The game can be paused using `ESC`.

The pause screen displays a dark overlay, title, separator, and resume instruction.

### Wave Complete

After all enemies in a wave are defeated, the game displays:

* Completed wave number
* Countdown to the next wave

### Game Over

When the player's health reaches zero, the Game Over screen displays:

* Final Score
* High Score
* Kill count
* Restart instruction

The game can be restarted using `R`.

---

## Player System

The player supports:

* WASD movement
* Shooting
* Health management
* Temporary invincibility after taking damage
* Shield protection
* Rapid Fire
* Health restoration through power-ups

Player configuration is centralized in `config/settings.py`.

---

## Enemy System

The game currently contains three enemy types.

### Normal Enemy

Balanced movement speed, health, damage, and score.

```text
Health: 30
Damage: 10
Score: 10
Speed: 50
```

### Fast Enemy

A faster enemy with lower health and zigzag movement.

```text
Health: 20
Damage: 15
Score: 20
Speed: 100
```

### Tank Enemy

A slower but stronger enemy with higher health and damage.

```text
Health: 50
Damage: 25
Score: 30
Speed: 30
```

Tank enemies also apply knockback when attacking the player.

Enemy configuration is centralized in `config/settings.py`.

---

## Wave System

Gameplay is divided into waves.

The initial wave contains 5 enemies.

Each completed wave increases the number of enemies:

```text
Starting enemies: 5
Enemies added per wave: 2
```

Enemy type probabilities change as the wave number increases, causing stronger enemy types to appear more frequently during later waves.

After completing a wave, a short countdown is displayed before the next wave starts.

---

## Combat System

### Shooting

The player fires bullets using `SPACE`.

Shooting uses a configurable cooldown.

Bullet properties such as speed, scale, and damage are centralized in `config/settings.py`.

### Collision

The game handles collisions between:

* Player and enemies
* Bullets and enemies
* Player and power-ups

Bullets are removed when they leave the playable area or successfully damage an enemy.

---

## Power-Up System

Enemies can drop power-ups when defeated.

### Health Power-Up

Restores a configurable amount of player health.

### Shield Power-Up

Temporarily protects the player from enemy damage.

### Rapid Fire Power-Up

Temporarily increases the player's firing speed.

Power-up textures are preloaded to avoid a delay when a power-up appears for the first time.

---

## Effects System

The game includes visual feedback systems such as:

* Explosions
* Particles
* Damage numbers
* Enemy health bars
* Player health bar
* Power-up status indicators

---

## Audio System

Audio is managed through `SoundManager`.

The system supports:

* Background music
* Sound effects
* Separate music volume
* Separate effects volume

Background music stops when Game Over is reached and starts again when the game is restarted.

---

## Score and High Score

The game tracks:

```text
Score
Kills
High Score
```

The High Score is stored locally in:

```text
data/high_score.txt
```

The file is created automatically when required.

It is excluded from version control through `.gitignore`, allowing each local installation to maintain its own High Score.

---

## Controls

| Key     | Action                  |
| ------- | ----------------------- |
| `W`     | Move Up                 |
| `A`     | Move Left               |
| `S`     | Move Down               |
| `D`     | Move Right              |
| `SPACE` | Shoot                   |
| `ESC`   | Pause / Resume          |
| `R`     | Restart after Game Over |

---

## Configuration

Gameplay and UI values are centralized in:

```text
config/settings.py
```

Examples include:

```text
PLAYER_SPEED
PLAYER_HEALTH
ENEMY_SPEED
ENEMY_HEALTH
BULLET_SPEED
BULLET_DAMAGE
SHOOT_COOLDOWN
WAVE_DELAY
POWER_UP_DROP_CHANCE
SHIELD_DURATION
RAPID_FIRE_DURATION
```

Centralizing these values makes gameplay balancing and future changes easier without modifying the main game logic.

---

## Resource Management

Resources are resolved through:

```text
config/paths.py
```

The project supports:

1. Running directly from Python source
2. Running as a PyInstaller build

The resource-path system is used for images, sounds, and persistent game data.

---

## Installation

### Requirements

* Python 3.11.2
* Arcade 3.3.3

Install Arcade:

```bash
pip install arcade==3.3.3
```

---

## Running From Source

Clone the repository:

```bash
git clone https://github.com/matinfate/arcade-first-game.git
cd arcade-first-game
```

Run the game:

```bash
python main.py
```

---

## Windows Build

The project uses PyInstaller to create a standalone Windows build.

Install PyInstaller:

```bash
pip install pyinstaller
```

Build the project:

```bash
pyinstaller --clean ArcadeGame.spec
```

The generated build is located at:

```text
dist/ArcadeGame/
```

Executable:

```text
dist/ArcadeGame/ArcadeGame.exe
```

The packaged version contains the required game assets and does not require Python or Arcade to be installed separately.

The application is configured as a windowed executable and does not open a separate console window.

---

## Development Principles

The project is developed incrementally with focus on:

* Separation of responsibilities
* Reusable classes
* Centralized configuration
* Predictable game-state transitions
* Modular resource management
* Reusable game systems
* Maintainable gameplay logic
* Standalone application packaging

---

## Future Development

Possible future improvements include:

* Additional enemy types
* New weapons
* Additional power-ups
* Boss encounters
* More advanced enemy AI
* Additional levels
* Additional game modes
* Improved animations
* Additional visual effects
* Further refactoring and optimization
* Additional progression systems

---

## Project Status

**Version 1.0**

The project currently contains a complete playable gameplay loop with multiple enemy types, wave progression, power-ups, visual effects, audio, persistent High Score, game-state management, and Windows packaging.

Development may continue with additional gameplay and architectural improvements.
