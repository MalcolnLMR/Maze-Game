# Malcoln Lucas Minson Rafael
import pygame as pg
from pygame.locals import *
from configs import getScreen

import player as pl
import tiles as tl

Screen = getScreen()
screenX = Screen[0]
screenY = Screen[1]

actualLevel = 1
Load = True
Win = False
player = pg.Rect(0, 0, 0, 0)

helpBox = pg.Rect(screenX/2 + 50, screenY - 50, 50, 10)
font = pg.font.Font('freesansbold.ttf', 18)

def changeMap(actualLevel):
	global player
	tl.resetMap()
	tl.loadMap(actualLevel)
	player = pl.player(pg.Rect(tl.spawnRects[0]))

def draw(gameState, canvas):
	try:			
		for obj in tl.objList:
			obj.draw(canvas)
		player.draw(canvas)
	except AttributeError:
		pass
	if actualLevel == 3:
		text_ini = font.render('ESC - para reiniciar', True, (255, 255, 255))
		canvas.blit(text_ini, helpBox)


def tick(gameState, dt):
	global actualLevel, Load, Win
	if gameState == "Game" and Load:
		changeMap(actualLevel)
		Load = False
	elif Win:
		actualLevel = 1
		changeMap(actualLevel)
		Load = False

	if player.win():		
		actualLevel += 1
		if actualLevel > 5:
			Win = True
			return "Win"
		Load = True

	


	player.tick(dt)	

	for event in pg.event.get():
			if event.type == pg.KEYDOWN:

				if event.key == K_UP:

					collider = player.rectUp.collidelist(tl.objList)
					if player.canMoveUp and not isinstance(tl.objList[collider], tl.wall) or collider < 0:
						
						if player.y <= 0:
							player.y = screenY - player.spd
						else:
							player.y -= player.spd
						player.canMoveUp = False

				elif event.key == K_DOWN:

					collider = player.rectDown.collidelist(tl.objList)
					if player.canMoveDown and not isinstance(tl.objList[collider], tl.wall) or collider < 0:
						if player.y >= screenY - player.spd:
							player.y = 0
						else:
							player.y += player.spd
						player.canMoveDown = False

				elif event.key == K_LEFT:

					collider = player.rectLeft.collidelist(tl.objList)
					if player.canMoveLeft and not isinstance(tl.objList[collider], tl.wall) or collider < 0:
						if player.x <= 0:
							player.x = screenX - player.spd
						else:
							player.x -= player.spd
						player.canMoveLeft = False

				elif event.key == K_RIGHT:

					collider = player.rectRight.collidelist(tl.objList)
					if player.canMoveRight and not isinstance(tl.objList[collider], tl.wall) or collider < 0:
						if player.x >= screenX - player.spd:
							player.x = 0 
						else:
							player.x += player.spd
						player.canMoveRight = False

				elif event.key == K_ESCAPE:
					actualLevel = 1
					Load = True

			if event.type == pg.KEYUP:
				if event.key == K_UP:
					player.canMoveUp = True
				elif event.key == K_DOWN:
					player.canMoveDown = True
				elif event.key == K_LEFT:
					player.canMoveLeft = True
				elif event.key == K_RIGHT:
					player.canMoveRight = True

			if event.type == QUIT:
				return "Quit"
	return gameState
