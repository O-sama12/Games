#Import necessary library
import pygame as pm
#Initializing Pygame
pm.init()
#Setting screen
screen = pm.display.set_mode((800, 500))
#Setting game caption
pm.display.set_caption("Space Invaders")
#Setting game Icon
icon = pm.image.load('ufo.png')
pm.display.set_icon(icon)
#Code for Game loop
running = True
while running:
    for event in pm.event.get():
        #Code for quitting game
        if event.type == pm.QUIT:
            running = False
    screen.fill((255, 82, 10))
    pm.display.update()
#Quitting the game
pm.quit()