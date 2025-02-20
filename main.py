import pygame
from constants import *
from player import Player

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    x = int(SCREEN_WIDTH / 2) 
    y = int(SCREEN_HEIGHT / 2)
    player = Player(x, y)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #limit FPS to 60    
        dt = clock.tick(60) / 1000

        player.update(dt)
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()


    


if __name__ == "__main__":
    main()