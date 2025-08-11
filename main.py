import sys
import pygame
import random
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, ASTEROID_MIN_RADIUS, BLACK
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = (updatables)
    Shot.containers = (updatables, drawables, shots)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidField = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(BLACK)

        updatables.update(dt)

        for asteroid in asteroids:
            if(asteroid.collidesWith(player)):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if(shot.collidesWith(asteroid)):
                    shot.kill()
                    asteroid.kill()
                    if asteroid.radius >= ASTEROID_MIN_RADIUS:
                        random_angle = random.uniform(20, 50)

                        first_rotation = asteroid.velocity.rotate(random_angle)
                        second_rotation = asteroid.velocity.rotate(-random_angle)

                        new_radius = asteroid.radius - ASTEROID_MIN_RADIUS

                        first_new_asteroid = Asteroid(asteroid.position.x, asteroid.position.y, new_radius)
                        second_new_asteroid = Asteroid(asteroid.position.x, asteroid.position.y, new_radius)

                        first_new_asteroid.velocity = first_rotation * 1.2
                        second_new_asteroid.velocity = second_rotation * 1.2


        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
