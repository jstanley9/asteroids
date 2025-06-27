import circleshape
import constants
import pygame
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, constants.WHITE, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            self.kill()
            return
        
        angle = random.uniform(20, 50)
        new_velocity = pygame.math.Vector2.length(self.velocity) * constants.ASTEROID_SPEED_UP
        vector_left = self.velocity.rotate(-angle)
        pygame.math.Vector2.scale_to_length(vector_left, new_velocity)
        vector_right = self.velocity.rotate(angle)
        pygame.math.Vector2.scale_to_length(vector_right, new_velocity)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        x = self.position.x
        y = self.position.y

        self.kill()
        spawn_left = Asteroid(x, y, new_radius)
        spawn_left.velocity = vector_left
        spawn_right = Asteroid(x, y, new_radius)
        spawn_right.velocity = vector_right
