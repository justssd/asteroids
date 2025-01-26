import pygame

from constants import *
from player import *

FRAMERATE = 60


def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, BLACK)
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(FRAMERATE) / 1000


if __name__ == "__main__":
    main()
