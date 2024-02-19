# Malcoln Lucas Minson Rafael
import pygame as pg
from pygame.locals import *

def initPygame():
    Screen = getScreen()
    pg.init()
    Canvas = pg.display.set_mode(Screen, 0, 32)
    pg.display.set_caption("Iniciando")
    return Canvas

######################## INPUT ########################

def getScreen():
    Configs = open("Configs.txt", "r")

    aux = Configs.readline().strip()
    listTemp = aux.split(';')
    screenX = int(listTemp[0])
    screenY = int(listTemp[1])

    Configs.close()

    return (screenX, screenY)

def getFps():    
    Configs = open("Configs.txt", "r")
    #pular primeira linha
    aux = Configs.readline().strip()
    
    aux = Configs.readline().strip()
    listTemp = aux.split(';')
    FPS = int(listTemp[0])

    Configs.close()

    return FPS

def getLevel(actualLevel):
    level = open("level_{}.txt".format(actualLevel), "r")
    lines = []
    for i in range(10):
        aux = level.readline().strip()        
        listTemp = aux.split(';')
        lines.append(listTemp)

    level.close()

    return lines
    
    
    

    
    
