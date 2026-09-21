# Arcade First Game 🎮

A 2D arcade shooter game built with Python and the [Arcade](https://api.arcade.academy/) library.

This project started as my first game development project and is focused on learning Python, Object-Oriented Programming (OOP), game architecture, collision systems, enemy behavior, game states, audio systems, resource management, and game packaging.

## Features

* 🎮 Main Menu and multiple game states
* 🕹️ WASD player movement
* 🔫 Shooting system with bullets
* ⏱️ Shooting cooldown
* ⚡ Rapid Fire power-up
* 🛡️ Shield power-up
* ❤️ Health power-up
* 👾 Multiple enemy types
* ⚡ Fast Enemy with zigzag movement
* 🛡️ Tank Enemy with high health and knockback
* ❤️ Player health system
* ❤️ Enemy health bars
* 💥 Explosion effects
* ✨ Particle effects
* 🔢 Damage numbers
* 🏆 Score system
* 🥇 Persistent High Score
* ☠️ Kill counter
* 🌊 Wave-based enemy spawning
* 📈 Increasing wave difficulty
* 🛡️ Player invincibility after taking damage
* 👾 Enemy collision avoidance
* 🎯 Safe enemy spawning away from the player
* ⏸️ Pause and Resume system
* 💀 Game Over screen
* 🔄 Game Restart system
* 🔊 Sound effects
* 🎵 Background music
* 🔉 Separate music and effects volume
* 🧩 Object-Oriented game structure
* ⚙️ Centralized game settings
* 📦 Standalone Windows executable support with PyInstaller

---

## Enemy System

The game currently contains three enemy types.

### Normal Enemy

* Balanced speed and health
* Score: 10
* Damage: 10

### Fast Enemy

* Higher movement speed
* Lower health
* Zigzag movement behavior
* Score: 20
* Damage: 15

### Tank Enemy

* Lower movement speed
* High health
* Higher damage
* Knockback effect when attacking the player
* Score: 30
* Damage: 25

Enemy properties such as speed, health, score, damage, and knockback are centralized in `config/settings.py`.

---

## Bullet System

The bullet system includes:

* Configurable bullet speed
* Configurable bullet scale
* Configurable bullet damage
* Automatic removal when bullets leave the screen
* Collision detection between bullets and enemies
* One bullet can damage only one enemy

Bullet-specific behavior is encapsulated inside the `Bullet` class.

---

## Power-Up System

Enemies have a chance to drop a power-up when defeated.

### Health Power-Up ❤️

Restores player health.

### Shield Power-Up 🛡️

Temporarily protects the player from enemy damage.

### Rapid Fire Power-Up ⚡

Temporarily increases the player's firing speed.

Power-up textures are preloaded to prevent a delay when a power-up appears for the first time.

---

## Wave System

The game uses a wave-based progression system.

* The first wave starts with 5 enemies.
* Each completed wave increases the number of enemies.
* Enemy type probabilities change as the wave number increases.
* Fast and Tank enemies become more common in later waves.
* A short countdown occurs between completed waves.
* A wave start sound is played when a new wave begins.

---

## Game States

The game currently supports:

* Main Menu
* Playing
* Paused
* Wave Complete
* Game Over
* Restart

---

## Audio System

The game includes a dedicated `SoundManager` responsible for managing game audio.

### Sound Effects

* Shooting
* Enemy death
* Player hit
* Power-up collection
* Wave start
* Game over

### Background Music

The game includes looping background music during gameplay.

Background music stops when the player reaches Game Over and starts again when the game is restarted.

Music and sound effects use separate volume settings.

---

## Score and High Score

The game tracks:

* Current Score
* Kill Count
* High Score

The High Score is stored locally in:

```text
data/high_score.txt
```

The file is automatically created when necessary and is ignored by Git so that each player can have their own local High Score.

---

## Controls

| Key   | Action                  |
| ----- | ----------------------- |
| W     | Move Up                 |
| A     | Move Left               |
| S     | Move Down               |
| D     | Move Right              |
| SPACE | Shoot                   |
| ESC   | Pause / Resume          |
| R     | Restart after Game Over |

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

### Architecture

The project separates different responsibilities into dedicated modules:

* `game.py` — Main game logic, game states, waves, collisions, scoring, and rendering
* `main.py` — Application entry point
* `entities/` — Game entities such as the player, enemies, bullets, particles, explosions, and power-ups
* `systems/` — Reusable game systems such as audio management
* `config/settings.py` — Centralized gameplay and window configuration
* `config/paths.py` — Resource path management for normal Python execution and PyInstaller builds
* `assets/` — Images and audio files
* `data/` — Local player data such as High Score
* `ArcadeGame.spec` — PyInstaller build configuration

---

## Resource Management

The project uses a centralized `resource_path()` function in `config/paths.py`.

This allows the game to correctly locate images and sound files in both situations:

1. Running directly from the Python source code
2. Running as a packaged PyInstaller executable

This is especially important because PyInstaller stores bundled resources inside the executable distribution directory.

---

## Running From Source

### Requirements

* Python 3.11.2
* Arcade 3.3.3

Install the required library:

```bash
pip install arcade==3.3.3
```

Run the game:

```bash
python main.py
```

---

## Building the Windows Executable

The project uses [PyInstaller](https://pyinstaller.org/) to create a standalone Windows build.

Install PyInstaller:

```bash
pip install pyinstaller
```

Build the game using the included specification file:

```bash
pyinstaller --clean ArcadeGame.spec
```

The packaged game will be generated inside:

```text
dist/ArcadeGame/
```

The main executable is:

```text
dist/ArcadeGame/ArcadeGame.exe
```

The packaged version includes the required game assets and does not require Python or Arcade to be installed on the target computer.

The game is configured as a windowed application, so launching the executable does not open a separate command-line window.

---

## Technologies

* Python
* Arcade
* Object-Oriented Programming
* PyInstaller
* Git
* GitHub
* PyCharm

---

## Project Goal

The main goal of this project is to learn the fundamentals of game development while improving Python and OOP skills through a practical project.

The project is developed incrementally, with a focus on:

* Clean architecture
* Reusable classes
* Separation of responsibilities
* Centralized configuration
* Game-state management
* Collision systems
* Enemy behavior
* Resource management
* Audio systems
* Packaging and distribution

---

## Future Plans

Possible future improvements include:

* 👾 More enemy types
* 🔫 More weapons
* ⚡ Additional power-ups
* 👹 Boss enemies
* 🎬 Improved animations
* 🧠 More advanced enemy AI
* 🗺️ Additional levels
* 🎮 Additional game modes
* ✨ More visual effects
* 🔧 Further code refactoring and optimization
* 🏅 Additional progression and scoring features

---

## Project Status

**Version 1.0 — Complete**

The first complete version of the game includes the core gameplay loop, multiple enemy types, waves, power-ups, visual effects, audio, pause and restart systems, persistent High Score, and Windows executable support.

The project may continue to receive new gameplay features and improvements as development continues.
