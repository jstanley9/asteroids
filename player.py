import circleshape
import constants
import pygame
import shot

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)

        self.rotation = 0
        self.shoot_cooldown = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]  

    def draw(self, screen):
        pygame.draw.polygon(screen, constants.WHITE, self.triangle(), 2 )

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt
    
    def rotate(self, delta):
        self.rotation += constants.PLAYER_TURN_SPEED * delta

    def shoot(self):
        bullet = shot.Shot(self.position.x, self.position.y)
        velocity = pygame.Vector2(0, 1).rotate(self.rotation) * constants.SHOT_SPEED
        bullet.velocity = velocity

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)     
        if keys[pygame.K_SPACE]:
            if self.shoot_cooldown <= 0:
                self.shoot()
                self.shoot_cooldown = constants.PLAYER_SHOT_COOLDOWN + dt
        
        self.shoot_cooldown -= dt