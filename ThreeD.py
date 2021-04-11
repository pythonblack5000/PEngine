import math
import time
import pygame
from pygame.locals import *


keys=[False]*324

worldMap =  [
			[1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
			[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
			[1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 3, 2, 3, 0, 0, 2],
			[2, 0, 3, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
			[1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
			[2, 3, 1, 0, 0, 2, 0, 0, 0, 2, 3, 2, 0, 0, 0, 0, 0, 0, 0, 1],
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 2, 0, 0, 0, 2],
			[2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 2, 1, 0, 0, 0, 1],
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 1, 0, 0, 0, 0, 0, 0, 0, 2],
			[2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
			[1, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
			[2, 0, 3, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 2, 1, 2, 0, 1],
			[1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 2],
			[2, 3, 1, 0, 0, 2, 0, 0, 2, 1, 3, 2, 0, 2, 0, 0, 3, 0, 3, 1],
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 2, 0, 0, 2],
			[2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 3, 0, 1, 2, 0, 1],
			[1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 3, 0, 2],
			[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1],
			[2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]]

def close(): 
	pygame.display.quit()
	pygame.quit()

def main():
	pygame.init()

	screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
	WIDTH, HEIGHT = screen.get_rect()[2:]
	pygame.display.set_caption("RayCast")
   
	
	positionX = 3.0
	positionY = 7.0

	directionX = 1.0
	directionY = 0.0

	planeX = 0.0
	planeY = 0.5

	ROTATIONSPEED = 0.007   
	MOVESPEED = 0.03

	TGM = (math.cos(ROTATIONSPEED), math.sin(ROTATIONSPEED))
	ITGM = (math.cos(-ROTATIONSPEED), math.sin(-ROTATIONSPEED))
	COS, SIN = (0,1)
	
	while True:
		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					close()
					return
				keys[event.key] = True
			elif event.type == KEYUP:
				keys[event.key] = False
  
		if keys[K_ESCAPE]:
			close()

		if keys[pygame.K_f]:
			oldDirectionX = directionX
			directionX = directionX * ITGM[COS] - directionY * ITGM[SIN]
			directionY = oldDirectionX * ITGM[SIN] + directionY * ITGM[COS]
			oldPlaneX = planeX
			planeX = planeX * ITGM[COS] - planeY * ITGM[SIN]
			planeY = oldPlaneX * ITGM[SIN] + planeY * ITGM[COS]

		if keys[pygame.K_g]:
			oldDirectionX = directionX
			directionX = directionX * TGM[COS] - directionY * TGM[SIN]
			directionY = oldDirectionX * TGM[SIN] + directionY * TGM[COS]
			oldPlaneX = planeX
			planeX = planeX * TGM[COS] - planeY * TGM[SIN]
			planeY = oldPlaneX * TGM[SIN] + planeY * TGM[COS]    

		if keys[pygame.K_w]:
			if not worldMap[int(positionX + directionX * MOVESPEED)][int(positionY)]:
				positionX += directionX * MOVESPEED
			if not worldMap[int(positionX)][int(positionY + directionY * MOVESPEED)]:
				positionY += directionY * MOVESPEED
				
		if keys[pygame.K_s]:
			if not worldMap[int(positionX - directionX * MOVESPEED)][int(positionY)]:
				positionX -= directionX * MOVESPEED
			if not worldMap[int(positionX)][int(positionY - directionY * MOVESPEED)]:
				positionY -= directionY * MOVESPEED
		
		if keys[pygame.K_a]:
			if not worldMap[int(positionX - directionY * MOVESPEED)][int(positionY)]:
				positionX += directionY * MOVESPEED
			if not worldMap[int(positionX)][int(positionY - directionX * MOVESPEED)]:
				positionY -= directionX * MOVESPEED
				
		if keys[pygame.K_d]:
			if not worldMap[int(positionX + directionY * MOVESPEED)][int(positionY)]:
				positionX -= directionY * MOVESPEED
			if not worldMap[int(positionX)][int(positionY + directionX * MOVESPEED)]:
				positionY += directionX * MOVESPEED


			

		
		pygame.draw.rect(screen, (103,200,224), (0, 0, WIDTH, HEIGHT/2))
		pygame.draw.rect(screen, (50,50,50), (0, HEIGHT/2, WIDTH, HEIGHT/2)) 
				 
		column = 0        
		while column < WIDTH:
			cameraX = 2.0 * column / WIDTH - 1.0
			rayPositionX = positionX
			rayPositionY = positionY
			rayDirectionX = directionX + planeX * cameraX
			rayDirectionY = directionY + planeY * cameraX + .000000000000001 # avoiding ZDE 

			mapX = int(rayPositionX)
			mapY = int(rayPositionY)

			deltaDistanceX = math.sqrt(1.0 + (rayDirectionY * rayDirectionY) / (rayDirectionX * rayDirectionX))
			deltaDistanceY = math.sqrt(1.0 + (rayDirectionX * rayDirectionX) / (rayDirectionY * rayDirectionY))

			if (rayDirectionX < 0):
				stepX = -1
				sideDistanceX = (rayPositionX - mapX) * deltaDistanceX

			else:
				stepX = 1
				sideDistanceX = (mapX + 1.0 - rayPositionX) * deltaDistanceX

			if (rayDirectionY < 0):
				stepY = -1
				sideDistanceY = (rayPositionY - mapY) * deltaDistanceY

			else:
				stepY = 1
				sideDistanceY = (mapY + 1.0 - rayPositionY) * deltaDistanceY

			hit = 0
			while  (hit == 0):
				if (sideDistanceX < sideDistanceY):
					sideDistanceX += deltaDistanceX
					mapX += stepX
					side = 0
					
				else:
					sideDistanceY += deltaDistanceY
					mapY += stepY
					side = 1
					
				if (worldMap[mapX][mapY] > 0):
					hit = 1

			if (side == 0):
				perpWallDistance = abs((mapX - rayPositionX + ( 1.0 - stepX ) / 2.0) / rayDirectionX)
			else:
				perpWallDistance = abs((mapY - rayPositionY + ( 1.0 - stepY ) / 2.0) / rayDirectionY)

			lineHEIGHT = abs(int(HEIGHT / (perpWallDistance+.0000001)))
			drawStart = -lineHEIGHT / 2.0 + HEIGHT / 2.0

			if (drawStart < 0):
				drawStart = 0

			drawEnd = lineHEIGHT / 2.0 + HEIGHT / 2.0

			if (drawEnd >= HEIGHT):
				drawEnd = HEIGHT - 1

			wallcolors = [ [], [150,0,0], [0,150,0], [0,0,150] ]
			color = wallcolors[ worldMap[mapX][mapY] ]                                                   
						
			pygame.draw.line(screen, color, (column,drawStart), (column, drawEnd), 2)
			column += 2

		pygame.event.pump()
		pygame.display.flip()           
	   
main()