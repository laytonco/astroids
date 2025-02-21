import pygame
import random
from constants import *
from  circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)
    
    def update(self, dt):
        self.position.x += self.velocity.x * dt
        self.position.y += self.velocity.y * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        new_asteroid_angle = random.uniform(20,50)
        a = self.velocity.rotate(new_asteroid_angle)
        b = self.velocity.rotate(-new_asteroid_angle)
        old_radius = self.radius
        new_radius = old_radius - ASTEROID_MIN_RADIUS

        new_asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_one.velocity = a * 1.2

        new_asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_two.velocity = b * 1.2

            


            

        

        