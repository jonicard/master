#snake.py

import pygame, sys, random
from pygame.math import Vector2

class FRUIT:
    def __init__(self):
        self.x=random.randint(0, cell_number -1)
        self.y=random.randint(0, cell_number -1)
        self.pos=Vector2(self.x,self.y)

    def draw_fruit(self):
        fruit_rect=pygame.Rect(self.pos.x*cell_size,self.pos.y*cell_size,cell_size,cell_size)
        pygame.draw.rect(screen,(126,166,114),fruit_rect)

        
pygame.init()
cell_size=20
cell_number=10
screen=pygame.display.set_mode((cell_size*cell_number,cell_size*cell_number))
clock=pygame.time.Clock()
test_surface= pygame.Surface((100,200))
test_rect=test_surface.get_rect(center=(200,250))
#setup window

#game logic
score=0
x_pos=200
fruit=FRUIT()
while True:
    for event in pygame.event.get():
         if event.type==pygame.QUIT:
             pygame.quit()
             sys.exit()
    
    screen.fill((175,215,70))
    fruit.draw_fruit()
    pygame.display.update()
    clock.tick(60)
    
