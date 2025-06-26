import pygame
from asteroid import *
from asteroidfield import *
from player import * 
from constants import *

def main():

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    delta = 0

    asteroids = pygame.sprite.Group() 
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (drawable, updatable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    drawable.add(player)
    updatable.add(player)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(constants.BLACK)  
        updatable.update(delta)
        for asteroid in asteroids:
            if player.are_colliding(asteroid):
                print("Game over!")
                return
            
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        delta_time = clock.tick(60)
        delta = delta_time / 1000

if __name__ == "__main__":
    main()