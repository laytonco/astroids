import pygame
from constants import *
def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        def fill(black):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            pygame.display.flip()

    


if __name__ == "__main__":
    main()