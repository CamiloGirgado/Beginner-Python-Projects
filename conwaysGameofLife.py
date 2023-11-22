# Conway's Game of Life

import random
import time
import copy

# Creates a list of list for the new cells
nextCells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append('#') #Adds a living cell
        else:
            column.append(' ') #Adds a dead cell
        nextCells.append(column) #Next cells is a list of clum lists

while True: #Main program loop
    print('\n\n\n\n') #Seperate each step with newlines
    currentCells = copy.deepcopy(nextCells)

    # Print the currentCells on the screen
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='') #Print the # or space
        print() # Print a new line at the end of the row
    
    # Calculate the next step's cells based on the current step's cells

    
        
