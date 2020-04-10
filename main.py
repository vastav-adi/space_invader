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

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerX_change = -0.5
			if event.key == pygame.K_RIGHT:
				playerX_change = 0.5

		# this is to stop the user when we stop pressing		
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0

		if event.type == pygame.QUIT:
			running = False

	# calls the function to draw the player over the screen
	playerX += playerX_change

	#login for boundary
	if playerX <= -10:
		playerX = -10
	if playerX >=746:
		playerX = 746
	player(playerX,playerY)
	pygame.display.update()

