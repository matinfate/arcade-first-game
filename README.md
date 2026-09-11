# Arcade First Game 🎮

A 2D arcade shooter game built with **Python** and the **Arcade** library.

This project is my first game development project and is focused on learning Python, Object-Oriented Programming (OOP), game architecture, collision systems, enemy behavior, power-ups, and game-state management.

## Features

* 🎮 Start menu and game states
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
* 🏆 Score system
* ☠️ Kill counter
* 🌊 Wave-based enemy spawning
* 📈 Increasing wave difficulty
* 🛡️ Player invincibility after taking damage
* 👾 Enemy collision avoidance
* 🎯 Safe enemy spawning away from the player
* ⏸️ Pause and resume system
* 💀 Game Over screen
* 🔄 Game restart system
* 🧩 Object-Oriented game structure
* ⚙️ Centralized game settings

## Enemy System

The game currently contains three enemy types:

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

Enemy properties such as speed, health, score, damage, and tank knockback are centralized in `settings.py`.

## Bullet System

The bullet system includes:

* Configurable bullet speed
* Configurable bullet scale
* Configurable bullet damage
* Automatic removal when bullets leave the screen
* Collision detection between bullets and enemies
* One bullet can damage only one enemy

Bullet-specific behavior is encapsulated inside the `Bullet` class.

## Power-Up System

Enemies have a chance to drop a power-up when defeated.

Current power-ups:

### Health Power-Up ❤️

Restores player health.

### Shield Power-Up 🛡️

Temporarily protects the player from enemy damage.

### Rapid Fire Power-Up ⚡

Temporarily increases the player's firing speed.

Power-up textures are preloaded to prevent a delay when a power-up appears for the first time.

## Wave System

The game uses a wave-based progression system.

* The first wave starts with 5 enemies.
* Each completed wave increases the number of enemies.
* Enemy type probabilities change as the wave number increases.
* Fast and Tank enemies become more common in later waves.
* A short delay occurs between completed waves.

## Game States

The game currently supports:

* Main Menu
* Playing
* Paused
* Wave Complete
* Game Over
* Restart

## Project Structure

```text
arcade-first-game/
│
├── main.py
├── game.py
├── player.py
├── enemy.py
├── bullet.py
├── explosion.py
├── particle.py
├── power_up.py
├── settings.py
├── README.md
│
└── assets/
    └── image/
        ├── player.png
        ├── enemy.png
        ├── fast_enemy.png
        ├── tank_enemy.png
        ├── bullet.png
        ├── health_powerup.png
        ├── shield_powerup.png
        └── rapid_fire_powerup.png
```

## Controls

| Key   | Action                  |
| ----- | ----------------------- |
| W     | Move Up                 |
| S     | Move Down               |
| A     | Move Left               |
| D     | Move Right              |
| SPACE | Shoot                   |
| ESC   | Pause / Resume          |
| R     | Restart after Game Over |

## Technologies

* **Python**
* **Arcade**
* **Object-Oriented Programming**
* **Git**
* **GitHub**
* **PyCharm**

## Project Goal

The main goal of this project is to learn the fundamentals of game development while improving my Python and OOP skills through a practical project.

The project is being developed incrementally, with a focus on clean architecture, reusable classes, centralized configuration, and gradually improving game systems.

## Future Plans

Possible future improvements include:

* More enemy types
* More weapons
* Additional power-ups
* Boss enemies
* Sound effects and background music
* Improved animations
* More advanced enemy AI
* Better menus and UI
* Additional levels and game modes
* Further code refactoring and optimization
