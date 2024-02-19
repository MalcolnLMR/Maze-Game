# Malcoln Lucas Minson Rafael
import pygame as pg
from pygame.locals import *

import tiles as tl
from configs import getScreen

Screen = getScreen()
screenX = Screen[0]
screenY = Screen[1]

class player:	
	def __init__(self, rect):
		self.spd = 50
		self.color = (20, 100, 100)
		self.rect = rect
		self.width = 50
		self.height = 50	
		self.canMove = True
		self.canMoveUp = True
		self.canMoveDown = True
		self.canMoveRight = True
		self.canMoveLeft = True	
		self.x = self.rect.x
		self.y = self.rect.y

	def setColliders(self):
		self.rectUp = pg.Rect(self.x, self.y - 50, self.width, self.height)
		self.rectDown = pg.Rect(self.x, self.y + 50, self.width, self.height)
		self.rectLeft = pg.Rect(self.x - 50, self.y, self.width, self.height)
		self.rectRight = pg.Rect(self.x + 50, self.y, self.width, self.height)
	

	def win(self):
		if isinstance(tl.objList[self.rect.collidelist(tl.objList)], tl.exit):
			return True
		else:
			return False

	def draw(self, canvas, sprite=0):
		if sprite == 0:
			pg.draw.rect(canvas, self.color, self.rect)
		else:
			canvas.blit(sprite, self.rect)

	def tick(self, dt):
		self.setColliders()
		self.rect = pg.Rect(self.x, self.y, self.width, self.height)




