# Malcoln Lucas Minson Rafael
import pygame as pg
from pygame.locals import *
from configs import *
from random import randint

######################## Declarações ########################
Screen = getScreen()
buttonWidth = 100
buttonHeigth = 40
flutuaction = 10
ScreenX = Screen[0] 
screenY = Screen[1]


buttonStart = pg.Rect(ScreenX/2 - buttonWidth/2 + 10, screenY/2 - buttonHeigth/2, buttonWidth, buttonHeigth)
buttonExit = pg.Rect(ScreenX/2 - 30 , screenY/2 + buttonHeigth, buttonWidth, buttonHeigth)
buttonExit2 = pg.Rect(ScreenX/2 - 20, screenY/2 + 20, buttonWidth, buttonHeigth)
winText = pg.Rect(ScreenX/2 - 100, screenY/2 - 60, buttonWidth, buttonHeigth)
title = pg.Rect(ScreenX/2 - 53, screenY/4, buttonWidth, buttonHeigth)
pg.font.init()
font = pg.font.Font('freesansbold.ttf', 18)


######################## Iniciando o menu ########################
def draw(gameState, canvas):
    if gameState == "Menu":
        
        text_ini = font.render('INICIAR', True, (255, 255, 255))
        canvas.blit(text_ini, buttonStart)

        text_ini = font.render('SAIR', True, (255, 255, 255))
        canvas.blit(text_ini, buttonExit)

        R = randint(-flutuaction, flutuaction)
        G = randint(-flutuaction, flutuaction)
        B = randint(-flutuaction, flutuaction)
        color = (100 + R, 100 + G, 100 + B)
        text_ini = font.render('O Labirinto', True, color)
        canvas.blit(text_ini, title)

    if gameState == "Win":
        text_ini = font.render('Parabéns, você ganhou!', True, (255, 255, 255))
        canvas.blit(text_ini, winText)

        text_ini = font.render('SAIR', True, (255, 255, 255))
        canvas.blit(text_ini, buttonExit2)

    
    pos = pg.mouse.get_pos()
    color = (randint(90, 100), randint(90, 100), randint(90, 100))
    pg.draw.circle(canvas, color, pos, 5)

def tick(gameState, dt):
    if gameState == "Menu":
        mousePos = pg.mouse.get_pos()
        if pg.mouse.get_pressed() == (1, 0, 0) and buttonStart.collidepoint(mousePos):
            return "Game"
        elif pg.mouse.get_pressed() == (1, 0, 0) and buttonExit.collidepoint(mousePos):
            return "Quit"
        return gameState
    elif gameState == "Win":
        mousePos = pg.mouse.get_pos()
        if pg.mouse.get_pressed() == (1, 0, 0) and buttonExit2.collidepoint(mousePos):
            return "Quit"
        return gameState

        