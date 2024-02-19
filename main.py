# Malcoln Lucas Minson Rafael

import math, time
import pygame as pg
from pygame.locals import *

import tiles as lv_01
import configs as config
import player
import menu
import levels as lv

gameloop = True
gameState = "Menu"

######################## Pygame ########################
Canvas = config.initPygame()

######################## Init FPS ########################
clock = pg.time.Clock()
FPS = 0
fpsCounter = 0
actualFPS = 0
configFPS = config.getFps()
prevTime = time.time()
clock.tick(FPS)
now = time.time()
dt = now - prevTime
prevTime = now

######################## Atualizações Globais ########################
def globalTick(displayFPS):
     title = "O Labirinto FPS: " + str(displayFPS)
     pg.display.set_caption(title)

while gameloop:
	Canvas.fill((150, 150, 150))

	clock.tick(configFPS)
	now = time.time()
	dt = now - prevTime
	prevTime = now

	FPS += 1
	fpsCounter += 1 * dt
	if fpsCounter >= configFPS * dt:
		actualFPS = FPS
		fpsCounter = 0
		FPS = 0


	if gameState == "Menu":
		menu.draw(gameState, Canvas)
		pg.display.update()
		gameState = menu.tick(gameState, dt)

	elif gameState == "Game":
		lv.draw(gameState, Canvas)           
		pg.display.update()
		gameState = lv.tick(gameState, dt)

	elif gameState == "Win":
		menu.draw(gameState, Canvas)
		pg.display.update()
		gameState = menu.tick(gameState, dt)

	elif gameState == "Quit":
		gameloop = False

	globalTick(actualFPS)
	for event in pg.event.get():
		if event.type == QUIT:
			gameloop = False

pg.display.quit()
print("Fim do Programa")