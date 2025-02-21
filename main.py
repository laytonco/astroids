import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot



def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    AsteroidField.containers = updatable
    astroid_field = AsteroidField()
    shots_group = pygame.sprite.Group()


    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots_group, updatable, drawable)

    x = int(SCREEN_WIDTH / 2) 
    y = int(SCREEN_HEIGHT / 2)
    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #limit FPS to 60    
        dt = clock.tick(60) / 1000

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
        for asteroid in asteroids:
            for shot in shots_group:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()
                    

        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        


    


if __name__ == "__main__":
    main()