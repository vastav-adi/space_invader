import pygame
import time

# initializing pygame
pygame.init()

# creating screen
screen = pygame.display.set_mode((800,600))

# title and Icon
icon = pygame.image.load("logos/logo.png")

pygame.display.set_caption("ASS INVADERS")
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load("user_image/user_bl.png")
playerX = 370
playerY = 480 
playerX_change = 0
playerY_change = 0

# draws the player
def player(x,y):
	screen.blit(playerImg,(x,y))

#game loop
running = True
while running:
	# RGB
	screen.fill((150,255,255))


	for event in pygame.event.get():

		if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				playerX -= 20
			if event.key == pygame.K_RIGHT:
				playerX += 20

		if event.type == pygame.QUIT:
			running = False

	# calls the function to draw the player over the screen
	player(playerX,playerY)
	pygame.display.update()

