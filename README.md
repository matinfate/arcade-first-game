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
