import sys
import os
import pygame
from pygame.locals import *

# Initialize the pygame
pygame.init()

# Set up display resolution
screen = pygame.display.set_mode((800, 600))

# Title
pygame.display.set_caption("Halma")

# Icon
icon = pygame.image.load(os.path.join(os.path.dirname(os.getcwd()),"img","icon","halma.png"))
pygame.display.set_icon(icon)

# Button setup
width = screen.get_width()
height = screen.get_height()
text_color = (255,255,255)
button_light = (32,32,32)
button_dark = (160,160,160)
text_font = pygame.font.SysFont('Arial',20)
text_one = text_font.render('8x8', True, text_color)
text_two = text_font.render('10x10', True, text_color)
text_three = text_font.render('16x16', True, text_color)

# Game loop
event_running = True
while event_running:
    # Screen background
    screen.fill((53,50,50))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            event_running = False
    
    # mouse coordinates
    mouse = pygame.mouse.get_pos()

    # Button event on hover
    # Button 1
    if width/2-50 <= mouse[0] <= width/2+50 and height/2 <= mouse[1] <= height/2+25:
        pygame.draw.rect(screen, button_dark, [width/2-50,height/2,100,25])
    else:
        pygame.draw.rect(screen, button_light, [width/2-50,height/2,100,25])
    # Button 2
    if width/2-50 <= mouse[0] <= width/2+50 and height/2+30 <= mouse[1] <= height/2+55:
        pygame.draw.rect(screen, button_dark, [width/2-50,height/2+30,100,25])
    else:
        pygame.draw.rect(screen, button_light, [width/2-50,height/2+30,100,25])
    # Button 3
    if width/2-50 <= mouse[0] <= width/2+50 and height/2+60 <= mouse[1] <= height/2+85:
        pygame.draw.rect(screen, button_dark, [width/2-50,height/2+60,100,25])
    else:
        pygame.draw.rect(screen, button_light, [width/2-50,height/2+60,100,25])

    # Generate button text
    screen.blit(text_one, (width/2-12,height/2))
    screen.blit(text_two, (width/2-22,height/2+30))
    screen.blit(text_three, (width/2-22,height/2+60))
    
    # Update display
    pygame.display.update()

pygame.quit()
sys.exit()