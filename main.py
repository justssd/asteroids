import pygame

from asteroid import *
from asteroidfield import *
from constants import *
from player import *

FRAMERATE = 60


def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid = pygame.sprite.Group()

    Asteroid.containers = (asteroid, updatable, drawable)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatable:
            obj.update(dt)
        pygame.Surface.fill(screen, BLACK)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(FRAMERATE) / 1000


if __name__ == "__main__":
    main()
