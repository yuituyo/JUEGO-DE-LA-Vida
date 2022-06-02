import pygame
import numpy as np
import time

pygame.init()

width, height = 1000, 1000

bg = 25, 25 ,25

screen  = pygame.display.set_mode((height, width))
screen.fill(bg)

# Tamaño de nuestra matriz
nxC, nyC = 60, 60

# Estado de las celdas. Viva = 1 / Muerta = 0
gameState = np.zeros((nxC,  nyC))

#dimensiones de cada celda individual
dimCW = width / nxC
dimCH = height / nyC

# DieHard
gameState[10, 10] = 1
gameState[10, 11] = 1
gameState[9, 10] = 1

gameState[13, 11] = 1
gameState[14, 11] = 1
gameState[15, 11] = 1

gameState[14, 9] = 1

#Pistola
gameState[30, 30] = 1

gameState[32, 30] = 1
gameState[32, 29] = 1

gameState[34, 28] = 1
gameState[34, 27] = 1
gameState[34, 26] = 1

gameState[36, 27] = 1
gameState[36, 26] = 1
gameState[36, 25] = 1
gameState[37, 26] = 1

#nave
gameState[50, 20] = 1
gameState[51, 20] = 1
gameState[52, 20] = 1
gameState[52, 19] = 1

gameState[51, 18] = 1


#nave2
gameState[20, 30] = 1
gameState[21, 30] = 1
gameState[22, 30] = 1
gameState[22, 29] = 1

gameState[21, 28] = 1


#pulsar
#y1
gameState[40,40] = 1
gameState[40,41] = 1
gameState[40,42] = 1
#x1
gameState[42,38] = 1
gameState[43,38] = 1
gameState[44,38] = 1

#y2
gameState[45,40] = 1
gameState[45,41] = 1
gameState[45,42] = 1
#x2
gameState[42,43] = 1
gameState[43,43] = 1
gameState[44,43] = 1

#p2
#y1
gameState[52,40] = 1
gameState[52,41] = 1
gameState[52,42] = 1
#x1
gameState[48,38] = 1
gameState[49,38] = 1
gameState[50,38] = 1

#y2
gameState[47,40] = 1
gameState[47,41] = 1
gameState[47,42] = 1
#x2
gameState[48,43] = 1
gameState[49,43] = 1
gameState[50,43] = 1

#pulsar2
#y1
gameState[40,46] = 1
gameState[40,47] = 1
gameState[40,48] = 1
#x1
gameState[42,45] = 1
gameState[43,45] = 1
gameState[44,45] = 1

#y2
gameState[45,46] = 1
gameState[45,47] = 1
gameState[45,48] = 1
#x2
gameState[42,50] = 1
gameState[43,50] = 1
gameState[44,50] = 1

#p2
#y1
gameState[47,46] = 1
gameState[47,47] = 1
gameState[47,48] = 1

#x1
gameState[48,45] = 1
gameState[49,45] = 1
gameState[50,45] = 1

#y2
gameState[52,46] = 1
gameState[52,48] = 1
gameState[52,47] = 1
#x2
gameState[48,50] = 1
gameState[49,50] = 1
gameState[50,50] = 1







pauseExect = False

# Bucle de ejecución
while True:

    # Copiamos la matriz del estado anterior
    # #para representar la matriz en el nuevo estado
    newGameState = np.copy(gameState)

    # Ralentizamos la ejecución a 0.1 segundos
    time.sleep(0.1)

    # Limpiamos la pantalla
    screen.fill(bg)

    # Registramos eventos de teclado y ratón.
    ev = pygame.event.get()

    # Cada vez que identificamos un evento lo procesamos
    for event in ev:
        # Detectamos si se presiona una tecla.
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect

        # Detectamos si se presiona el ratón.
        mouseClick = pygame.mouse.get_pressed()

        if sum(mouseClick) > 0:
            posX, posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX / dimCW)), int(np.floor(posY / dimCH))
            newGameState[celX, celY] = 1

    for y in range(0, nxC):
        for x in range (0, nyC):

            if not pauseExect:

                # Calculamos el número de vecinos cercanos.
                n_neigh =   gameState[(x - 1) % nxC, (y - 1)  % nyC] + \
                            gameState[(x)     % nxC, (y - 1)  % nyC] + \
                            gameState[(x + 1) % nxC, (y - 1)  % nyC] + \
                            gameState[(x - 1) % nxC, (y)      % nyC] + \
                            gameState[(x + 1) % nxC, (y)      % nyC] + \
                            gameState[(x - 1) % nxC, (y + 1)  % nyC] + \
                            gameState[(x)     % nxC, (y + 1)  % nyC] + \
                            gameState[(x + 1) % nxC, (y + 1)  % nyC]

                # Regla #1 : Una celda muerta con exactamente 3 vecinas vivas, "revive".

                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1

                # Regla #2 : Una celda viva con menos de 2 o más 3 vecinas vinas, "muere".

                elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0

            # Calculamos el polígono que forma la celda.
            poly = [((x)   * dimCW, y * dimCH),
                    ((x+1) * dimCW, y * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH),
                    ((x)   * dimCW, (y+1) * dimCH)]

            # Si la celda está "muerta" pintamos un recuadro con borde gris
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (40, 40, 40), poly, 1)
           # Si la celda está "viva" pintamos un recuadro relleno de color
            else:
                pygame.draw.polygon(screen, (200, 100, 100), poly, 0)

    # Actualizamos el estado del juego.
    gameState = np.copy(newGameState)

    # Mostramos el resultado
    pygame.display.flip()