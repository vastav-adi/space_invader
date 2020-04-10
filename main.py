import pygame

# initializing pygame
pygame.init()

# creating screen
screen = pygame.display.set_mode((800,600))

# title and Icon
icon = pygame.image.load("logos/logo.png")

pygame.display.set_caption("ASS INVADERS")
pygame.display.set_icon(icon)

#game loop
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False


	# RGB
	screen.fill((255,0,0))
	pygame.display.update()