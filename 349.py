#************************************************
# Rules of the game
#   1. If the ant is on a black square, it turns
#       right 90 and moves forward one unit
#   2. If the ant is on a white square, it turns
#       left 90 and moves forward one unit
#   3. When the ant leaves a square, it inverts
#       colour
#
# SEE: http://mathworld.wolfram.com/LangtonsAnt.html
#************************************************
 
import sys, pygame
from pygame.locals import *
import time
 
dirs = (
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
        )
 
cellSize = 5 # size in pixels of the board (4 pixels are used to draw the grid)
numCells = 130 # length of the side of the board
background = 0, 0, 0 # background colour; black here
foreground = 23, 23, 23 # foreground colour; the grid's colour; dark gray here
textcol = 177, 177, 177 # the colour of the step display in the upper left of the screen
antwalk = 44, 88, 44 # the ant's trail; greenish here
antant = 222, 44, 44 # the ant's colour; red here
fps = 1.0 / 300 # time between steps; 1.0 / 40 means 40 steps per second
 
def main():
    pygame.init()
 
    size = width, height = numCells * cellSize, numCells * cellSize
 
    pygame.display.set_caption("Langton's Ant")
 
    screen = pygame.display.set_mode(size) # Screen is now an object representing the window in which we paint
    screen.fill(background)
    pygame.display.flip() # IMPORTANT: No changes are displayed until this function gets called
 
    for i in xrange(1, numCells):
        pygame.draw.line(screen, foreground, (i * cellSize, 1), (i * cellSize, numCells * cellSize), 2)
        pygame.draw.line(screen, foreground, (1, i * cellSize), (numCells * cellSize, i * cellSize), 2)
    pygame.display.flip() # IMPORTANT: No changes are displayed until this function gets called
 
    font = pygame.font.Font(None, 36)
 
    antx, anty = numCells / 2, numCells / 2
    antdir = 0
    board = [[False] * numCells for e in xrange(numCells)]
 
    step = 1
    pause = False
    while True:
        for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYUP:
                    if event.key == 32: # If space pressed, pause or unpause
                        pause = not pause
                    elif event.key == 115:
                        pygame.image.save(screen, "Step%d.tga" % (step))
 
        if pause:
            time.sleep(fps)
            continue
 
        text = font.render("%d " % (step), True, textcol, background)
        screen.blit(text, (10, 10))
         
        if board[antx][anty]:
            board[antx][anty] = False # See rule 3
            screen.fill(background, pygame.Rect(antx * cellSize + 1, anty * cellSize + 1, cellSize - 2, cellSize - 2))
            antdir = (antdir + 1) % 4 # See rule 1
        else:
            board[antx][anty] = True # See rule 3
            screen.fill(antwalk, pygame.Rect(antx * cellSize + 1, anty * cellSize + 1, cellSize - 2, cellSize - 2))
            antdir = (antdir + 3) % 4 # See rule 2
 
        antx = (antx + dirs[antdir][0]) % numCells
        anty = (anty + dirs[antdir][1]) % numCells
 
        # The current square (i.e. the ant) is painted a different colour
        screen.fill(antant, pygame.Rect(antx * cellSize + 1, anty * cellSize + 1, cellSize -2, cellSize -2))
 
        pygame.display.flip() # IMPORTANT: No changes are displayed until this function gets called
 
        step += 1
        time.sleep(fps)
 
if __name__ == "__main__":
    main()
