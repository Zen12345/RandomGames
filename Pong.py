import pygame
from pygame.locals import *
pygame.init()
pygame.display.set_caption("Pong")
display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
    pygame.display.update()