import pygame
from pygame import mixer
import random
import math

# initializing pygame
pygame.init()

# creating screen
screen = pygame.display.set_mode((800,600))

# title and Icon
icon = pygame.image.load("logos/logo.png")
bg = pygame.image.load("user_image/background.png")
	
#adding bg music
mixer.music.load("Sounds/background.wav")
mixer.music.play(-1)

pygame.display.set_caption("CORONA INVADERS")
pygame.display.set_icon(icon)


# player
playerImg = pygame.image.load("user_image/user_bl.png")
playerX = 370
playerY = 480 
playerX_change = 0

# enemy
enemyImg = []
enmX = []
enmY = []
enmX_change = []
enmY_change = []
n = 6

# multiple enemies
for i in range(n):
	enemyImg.append(pygame.image.load("user_image/corona.png"))
	enmX.append(random.randint(20,735))
	enmY.append(random.randint(50,150))
	enmX_change.append(4)
	enmY_change.append(40)

# bullet
bulletImg = pygame.image.load("user_image/bullet.png")
bultX = 370
bultY = 480
bultY_change = -9
bullet_state = "ready"

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 15
textY = 15





# draws the player
def player(x,y):
	screen.blit(playerImg,(x,y))

def enemy(x,y,i):
	screen.blit(enemyImg[i],(x,y))

def fire_bullet(x,y):
	global bullet_state
	bullet_state = "fire"
	screen.blit(bulletImg,(x+25,y+10))

# collision
def isCollision(enmX,enmY,bultX,bultY):
	dist = math.sqrt(math.pow(enmX-bultX,2)+math.pow(enmY-bultY,2))
	if(dist<27):
		return True

# show score
def show_score(x,y):
	score = font.render("Score : " + str(score_value),True,(255,255,255))
	screen.blit(score,(x,y))






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
					bult_sound = mixer.Sound('Sounds/laser.wav')
					bult_sound.play()
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


	
	for i in range(n):

		enmX[i] += enmX_change[i]
		if enmX[i] <= -10:
			enmX_change[i] = 3
			enmY[i] += enmY_change[i]
		if enmX[i] >=746:
			enmX_change[i] = -3
			enmY[i] += enmY_change[i]

		# check for collision // collision mechanics
		collision = isCollision(enmX[i],enmY[i],bultX,bultY)
		if collision:
			# wow wow sound
			expl_sound = mixer.Sound('Sounds/explosion.wav')
			expl_sound.play()

			# 1. reset bullet
			bultY = 480
			bullet_state = "ready"

			#  2. set score
	
			score_value += 1
			
			# 3. respawn corona
			enmX[i] = random.randint(20,735)
			enmY[i] = random.randint(50,150)

		# bliting the enemy
		enemy(enmX[i],enmY[i],i)	
	



	# bullet movement
	if bultY <= 0:
		bultY = 480
		bullet_state = "ready"

	if bullet_state is "fire":
		fire_bullet(bultX,bultY)
		bultY = bultY + bultY_change 



	player(playerX,playerY)
	show_score(textX,textY)
	pygame.display.update()

