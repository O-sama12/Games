#Import necessary library
import pygame as pm
#Initializing Pygame
pm.init()
#Setting screen
width = 800
height = 600
screen = pm.display.set_mode((width, height))
#Setting game caption
pm.display.set_caption("Space Invaders")
#Setting game Icon
icon = pm.image.load('ufo.png')
pm.display.set_icon(icon)
#Adding player to the game
player_Img = pm.image.load('spaceship.png')
rocket_width, rocket_height = player_Img.get_size()
playerX = (width - rocket_width) // 2
playerY = height - rocket_height - 10 
def player():
    screen.blit(player_Img, (playerX, playerY))
#Code for Game loop
running = True
while running:
    for event in pm.event.get():
        #Screen coloring
        screen.fill((0, 0, 0))
        #Code for quitting game
        if event.type == pm.QUIT:
            running = False
    player()
    pm.display.update()
#Quitting the game
pm.quit()