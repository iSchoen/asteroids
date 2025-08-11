# Asteroids Game

A Python implementation of the classic Asteroids arcade game built with Pygame. Navigate your triangular ship through space, destroy asteroids, and avoid collisions.

## Controls

- **W** - Move forward (thrust)
- **S** - Move backward
- **A** - Rotate left
- **D** - Rotate right
- **SPACE** - Shoot

## Installation

This project requires Python 3.12+ and pygame.

### Using uv (recommended)

```bash
uv sync
```

### Using pip

```bash
pip install pygame==2.6.1
```

## Running the Game

```bash
python main.py
```

## How to Play

1. Use WASD keys to maneuver your triangular ship
2. Press SPACE to fire projectiles at asteroids
3. Large asteroids split into smaller pieces when shot
4. Avoid colliding with asteroids - the game ends on contact
5. New asteroids continuously spawn from the screen edges
