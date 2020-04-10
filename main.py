import pygame
import random
import math

# initializing pygame
pygame.init()

# creating screen
screen = pygame.display.set_mode((800,600))

score = 0

# title and Icon
icon = pygame.image.load("logos/logo.png")
bg = pygame.image.load("user_image/background.png")


pygame.display.set_caption("CORONA INVADERS")
pygame.display.set_icon(icon)


# player
playerImg = pygame.image.load("user_image/user_bl.png")
playerX = 370
playerY = 480 
playerX_change = 0

# enemy
enemyImg = pygame.image.load("user_image/corona.png")
enmX = random.randint(20,735)
enmY = random.randint(50,150) 
enmX_change = 3
enmY_change = 64

# bullet
bulletImg = pygame.image.load("user_image/bullet.png")
bultX = 370
bultY = 480
bultY_change = -10
bullet_state = "ready"




# draws the player
def player(x,y):
	screen.blit(playerImg,(x,y))

def enemy(x,y):
	screen.blit(enemyImg,(x,y))

def fire_bullet(x,y):
	global bullet_state
	bullet_state = "fire"
	screen.blit(bulletImg,(x+25,y+10))




# collision
def isCollision(enmX,enmY,bultX,bultY):
	dist = math.sqrt(math.pow(enmX-bultX,2)+math.pow(enmY-bultY,2))
	if(dist<27):
		return True



#game loop
running = True
while running:
	# RGB
	screen.fill((150,255,255))
	screen.blit(bg,(0,0))


	for event in pygame.event.get():

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerX_change = -5
			if event.key == pygame.K_RIGHT:
				playerX_change = 5

			if event.key == pygame.K_SPACE:
				if bullet_state is "ready":
					bultX = playerX
					fire_bullet(bultX,bultY)

		# this is to stop the user when we stop pressing		
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0

		if event.type == pygame.QUIT:
			running = False

	playerX += playerX_change

	#logic for boundary
	if playerX <= -10:
		playerX = -10
	if playerX >=746:
		playerX = 746

	
	enmX += enmX_change

	if enmX <= -10:
		enmX_change = 3
		enmY += enmY_change
	if enmX >=746:
		enmX_change = -3
		enmY += enmY_change


	# bullet movement
	if bultY <= 0:
		bultY = 480
		bullet_state = "ready"

	if bullet_state is "fire":
		fire_bullet(bultX,bultY)
		bultY = bultY + bultY_change 




	# check for collision // collision mechanics
	collision = isCollision(enmX,enmY,bultX,bultY)
	if collision:
		# 1. reset bullet
		bultY = 480
		bullet_state = "ready"

		# 2. set score
		score += 1
		print(score)
		
		# 3. respawn corona
		enmX = random.randint(20,735)
		enmY = random.randint(50,150) 


	enemy(enmX,enmY)	
	player(playerX,playerY)
	pygame.display.update()

