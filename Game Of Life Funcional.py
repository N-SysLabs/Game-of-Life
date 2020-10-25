#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygame
import numpy as np
import time as T
import sys
pygame.init ()


# In[ ]:


#Pantalla
width, height = (1000,1000)
screen = pygame.display.set_mode((width, height))

#Color
bg=(25,25,25)

#Pintamos el fondo
screen.fill(bg)

#Numero de celdas
nxC, nyC = 50,50

#Dimensiones de la celda
dimCW = width  / nxC
dimCH = height / nyC

#Estado de las celdas. <viva> = 1, <muerta> = 0
gameState = np.zeros ((nxC, nyC))

#Control de la ejecucion del juego
pauseExect = False

#Logica del Juego
while True:
    
    #Metodo de salida
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    #Actualizacion del Estado del Juego        
    newGameState = np.copy(gameState)
    screen.fill(bg)
    T.sleep(0.1)
    
    #Registramos el teclado y ratón.
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect
        
        mouseClick = pygame.mouse.get_pressed()
        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX/dimCW)), int(np.floor(posY/dimCH))
            newGameState [celX, celY] = not mouseClick [2]
            
    #Malla del juego
    for y in range(0, nxC):
        for x in range(0, nyC):
            
            if not pauseExect:
            
                #Calculamos el numero de vecinos cencanos.
                n_neigh = gameState [(x - 1) % nxC, (y - 1) % nyC] +                               gameState [(x)     % nxC, (y - 1) % nyC] +                               gameState [(x + 1) % nxC, (y - 1) % nyC] +                               gameState [(x - 1) % nxC, (y) % nyC] +                               gameState [(x + 1) % nxC, (y) % nyC] +                               gameState [(x - 1) % nxC, (y + 1) % nyC] +                               gameState [(x)     % nxC, (y + 1) % nyC] +                               gameState [(x + 1) % nxC, (y + 1) % nyC]
                #Regla 1:
                if gameState [x, y] == 0 and n_neigh == 3:
                    newGameState [x, y] = 1

                #Regla 2:
                elif gameState [x, y] == 1 and (n_neigh < 2 or n_neigh >3):
                    newGameState [x, y] = 0

            #Poligono de cada celda
            poly= [((x)  * dimCW, y * dimCH),
                   ((x+1)* dimCW, y * dimCH),
                   ((x+1)* dimCW, (y+1) * dimCH),
                   ((x)  * dimCW, (y+1) * dimCH)]
            
            #Dibujamos las celdas X,Y
            if newGameState [x,y] == 0:
                pygame.draw.polygon (screen,(128,128,128), poly, 1)
            else:
                pygame.draw.polygon (screen,(255,255,255), poly, 0)
    #Actualizamos el estado del juego
    gameState= np.copy(newGameState)
    #Actualizamos la pantalla
    pygame.display.flip()
    
#Coded by Samuel.
#In Memory of John Horton Conway. The original creator of this game.


# In[ ]:




