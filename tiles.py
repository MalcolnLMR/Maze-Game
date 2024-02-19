# Malcoln Lucas Minson Rafael
import configs
import pygame as pg
from pygame.locals import *

class tile:
	def __init__(self):
		self.width = 50
		self.height = 50

	def draw(self, canvas, sprite=0):
		if sprite == 0 and self.drawnable:
			pg.draw.rect(canvas, self.color, self.rect)
		elif self.drawnable:
			canvas.blit(sprite, self.rect)

class floor(tile):
	def __init__(self, posX, posY):
		tile.__init__(self)
		self.color = (200, 200, 200)		
		self.collision = False
		self.drawnable = True
		self.moveThrough = True
		self.x = posX
		self.y = posY
		self.rect = pg.Rect(self.x, self.y, self.width, self.height)

class wall(tile):
	def __init__(self, posX, posY):
		tile.__init__(self)
		self.color = (100,100,100)	
		self.collision = True
		self.drawnable = True
		self.moveThrough = False
		self.x = posX
		self.y = posY
		self.rect = pg.Rect(self.x, self.y, self.width, self.height)

class spawn(tile):
	def __init__(self, posX, posY):
		tile.__init__(self)
		self.color = (0, 20, 255)		
		self.collision = False
		self.drawnable = False
		self.moveThrough = True
		self.x = posX
		self.y = posY
		self.rect = pg.Rect(self.x, self.y, self.width, self.height)

class way(tile):
	def __init__(self, posX, posY):
		tile.__init__(self)
		self.color = (255, 255, 255)		
		self.collision = True
		self.drawnable = True
		self.moveThrough = True
		self.x = posX
		self.y = posY
		self.rect = pg.Rect(self.x, self.y, self.width, self.height)

class exit(tile):
	def __init__(self, posX, posY):
		tile.__init__(self)
		self.color = (200, 50, 50)		
		self.collision = True
		self.drawnable = True
		self.moveThrough = True
		self.x = posX
		self.y = posY
		self.rect = pg.Rect(self.x, self.y, self.width, self.height)


spawnRects = []
objList = []

def resetMap():
	global spawnRects, objList
	spawnRects = []
	objList = []


def loadMap(actualLevel):
	global wallRects, floorRects, spawnRects, wayRects, exitRects, objList
	level = configs.getLevel(actualLevel)

	for x in range(10):
		for y in range(20):
			if level[x][y] == "0": #chão		
				new = floor(y*50, x*50)
				objList.append(new)
			elif level[x][y] == "1": #Parede
				new = wall(y*50, x*50)
				objList.append(new)
			elif level[x][y] == "2": #Spawn
				new = spawn(y*50, x*50)
				spawnRects.append(new)
				new = floor(y*50, x*50)
				objList.append(new)
			elif level[x][y] == "3": #Reentradas
				new = way(y*50, x*50)
				objList.append(new)
			elif level[x][y] == "4": #Saida
				new = exit(y*50, x*50)
				objList.append(new)
