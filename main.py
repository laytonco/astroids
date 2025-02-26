import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from button import Button



def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    pygame.init()
    

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    score = 0
    #game over condition set to false (used in printing game over screen)
    game_over = 0
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    AsteroidField.containers = updatable
    astroid_field = AsteroidField()
    shots_group = pygame.sprite.Group()



     ## game over splash screen
    restart_font = pygame.font.Font(None, 36)
    go_font = pygame.font.Font(None, 52)
    go_text = go_font.render(f"Game over!!", True, "white")
    go_text_width, go_text_height = go_text.get_size()
    game_over_position = ((1280 - go_text_width) // 2, (720 - go_text_height) // 2)
    final_score_text = go_font.render(f"Final Score:{score} ", True, "white")
    final_score_text_position = (game_over_position[0], game_over_position[1] + go_text_height + 10)

   
  

    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots_group, updatable, drawable)

    x = int(SCREEN_WIDTH / 2) 
    y = int(SCREEN_HEIGHT / 2)
    player = Player(x, y)

    restart_button = Button(10, SCREEN_HEIGHT - 60, 100, 50, "Restart", restart_font, "white", "grey")

    #game loop
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #limit FPS to 60    
        dt = clock.tick(60) / 1000

        updatable.update(dt)
        ## collision detection
        for asteroid in asteroids:
            if asteroid.collides_with(player): 
               game_over = 1 
               print("Game over!")
               #sys.exit()
        for asteroid in asteroids:
            for shot in shots_group:
                if asteroid.collides_with(shot):
                    
                    score += 100
                    asteroid.split()
                    shot.kill()
        ## scoring system
        score_font = pygame.font.Font(None, 36)
        score_text = score_font.render(f"Score:{score} ", True, "white")
        #for splash screen
        final_score_text = go_font.render(f"Final Score:{score} ", True, "white")
        text_width, text_height = score_text.get_size()
        score_position = (SCREEN_WIDTH - text_width, 0)
             

        screen.fill("black")
        #score display
        screen.blit(score_text, score_position)
        #game over screen
        if game_over == 1:
            screen.blit(go_text, game_over_position)
            screen.blit(final_score_text, final_score_text_position)
            restart_button.draw(screen)
            if restart_button.is_clicked():
                main()
                return
            for asteroid in asteroids:
                asteroid.kill()
            for player in updatable:
                player.kill()
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        


    


if __name__ == "__main__":
    main()