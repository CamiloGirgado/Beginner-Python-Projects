# Conway's Game of Life

import random
import time
import copy

WIDTH = 60
HEIGHT = 20


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

    for x in range(WIDTH):
        for y in range (HEIGHT):
            # Get neighbors
            # '% WIDTH' ensures leftCoord is always between 0 and WIDTH - 1
            leftCoord  =  (x - 1) % WIDTH
            rightCoord =  (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            #Count the number of living neighbors
            numNeighbors = 0
            if currentCells[leftCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top Left is alive
            if currentCells[leftCoord][y] == '#':
                numNeighbors += 1 # Left is alive
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom Left is alive
            if currentCells[x][belowCoord] == '#':
                numNeighbors += 1 # Bottom is alive
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbors += 1 # Bottom Right is alive
            if currentCells[rightCoord][y] == '#':
                numNeighbors += 1 # Right is alive
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbors += 1 # Top Right is alive\
            if currentCells[x][aboveCoord] == '#':
                numNeighbors += 1 # Top is alive

            # Set cells based on Conway's Game of Life Rules
            if currentCells[x][y] == '#' and (numNeighbors == 2 or numNeighbors == 3):
                #Living cells with 2 or 3 neighbors stay alive
                nextCells[x][y] = '#'
            elif currentCells == ' ' and numNeighbors == 3:
                # Dead cells with 3 neighbors become alive
                nextCells[x][y] = '#'
            else:
                # Everything else dies or stays dead:
                nextCells[x][y] = ' '
        time.sleep(1) # Add a one second pause to reduce flickering
            
            




    
        
