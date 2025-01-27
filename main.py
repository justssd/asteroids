import pygame
import sys

from asteroid import *
from asteroidfield import *
from constants import *
from player import *
from shot import *

FRAMERATE = 60


def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    Player.containers = (updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group,)
    Shot.containers = (updatable_group, drawable_group, shot_group)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatable_group:
            obj.update(dt)
        for asteroid in asteroid_group:
            if asteroid.collides(player):
                print("Game over!")
                sys.exit()
            for shot in shot_group:
                if asteroid.collides(shot):
                    asteroid.split()
                    shot.kill()
        pygame.Surface.fill(screen, BLACK)
        for obj in drawable_group:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(FRAMERATE) / 1000


if __name__ == "__main__":
    main()
