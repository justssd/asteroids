import random

from circleshape import *
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Split asteroid into two smaller but faster asteroids
        split_angle = random.uniform(20, 50)
        split_radius = self.radius - ASTEROID_MIN_RADIUS
        split_1 = Asteroid(self.position.x, self.position.y, split_radius)
        split_2 = Asteroid(self.position.x, self.position.y, split_radius)
        split_1.velocity = self.velocity.rotate(split_angle) * 1.2
        split_2.velocity = self.velocity.rotate(-split_angle) * 1.2

    def draw(self, screen):
        pygame.draw.circle(screen, GREEN, self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
